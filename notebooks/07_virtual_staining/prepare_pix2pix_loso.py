"""Prepare leave-one-BIOLOGICAL-sample-out pix2pix folds from cropped images

Usage:
  python prepare_pix2pix_loso.py --list
  python prepare_pix2pix_loso.py --dataset HE_TRI --test-sample SAMPLE
  python prepare_pix2pix_loso.py --all --link-mode copy

Each fold has train/, val/, test/ containing 1024x512 aligned A|B PNGs
for the official pytorch-CycleGAN-and-pix2pix dataset_mode=aligned.
Use --link-mode hardlink to save disk space when the filesystem supports it.
"""
from __future__ import annotations
import argparse
import csv
import os
import shutil
from pathlib import Path
from PIL import Image

SAMPLES = {
    'HE_TRI': [],
    'HE_PAS': [],
}
COUNTS = {} # key: sample  name, value: number of images per sample
DEFAULT_ROOT = Path(r'')

def sample_paths(root, ds, sample):
    folder = root / ds / sample
    a = folder / 'A'
    b = folder / 'B'
    ab = folder / 'AB'
    if not a.is_dir() or not b.is_dir():
        raise FileNotFoundError(f'Missing sample A/B folders: {folder}')
    names_a = {p.name for p in a.glob('*.png')}
    names_b = {p.name for p in b.glob('*.png')}
    expected = {f'{i:06d}.png' for i in range(COUNTS[sample])}
    if names_a != names_b or names_a != expected:
        raise ValueError(f'{folder}: A/B mismatched or crop count/filenames are not as expected: '
                         f'A={len(names_a)}, B={len(names_b)}, expected={len(expected)}')
    return folder, ab, sorted(expected)

def materialize(src: Path, dst: Path, mode: str):
    if mode == 'hardlink':
        try:
            os.link(src,dst)
        except OSError as e:
            raise OSError(f'Cannot hardlink {src} to {dst}; use --link-mode copy') from e
    elif mode == 'symlink':
        try:
            os.symlink(src.resolve(),dst)
        except OSError as e:
            raise OSError('Symlinks are unavailable; use --link-mode copy') from e
    else:
        shutil.copy2(src,dst)

def build_one(root:Path, output:Path, ds:str, holdout:str, mode:str):
    samples = SAMPLES[ds]
    if holdout not in samples:
        raise ValueError(f'{holdout} is not in {ds} sample list')
    # Deterministic round-robin biological-sample validation.
    val = samples[(samples.index(holdout)+1) % len(samples)]
    train = [s for s in samples if s not in (holdout,val)]
    fold = output / ds / f'test_{holdout}'
    if fold.exists():
        raise FileExistsError(f'Output fold already exists, refusing to mix files: {fold}')
    # Prevalidate all sample files and total pairs before creating output.
    info={s:sample_paths(root,ds,s) for s in samples}
    fold.mkdir(parents=True)
    manifest=[]
    try:
        for split, split_samples in [('train',train),('val',[val]),('test',[holdout])]:
            dest_dir=fold/split
            dest_dir.mkdir()
            for sample in split_samples:
                folder, ab_dir, names=info[sample]
                for name in names:
                    dest=f'{sample}__{name}'
                    src_ab=ab_dir/name
                    dst=dest_dir/dest
                    if src_ab.exists():
                        # Existing AB files were created A-left, B-right.
                        materialize(src_ab,dst,mode)
                    else:
                        # Avoid dependence on an AB folder.
                        with Image.open(folder/'A'/name) as a_im, Image.open(folder/'B'/name) as b_im:
                            a=a_im.convert('RGB'); b=b_im.convert('RGB')
                            if a.size != b.size:
                                raise ValueError(f'Pair shape mismatch {folder} {name}')
                            combined=Image.new('RGB',(a.width+b.width,a.height))
                            combined.paste(a,(0,0)); combined.paste(b,(a.width,0))
                            combined.save(dst)
                    manifest.append((ds,holdout,val,split,sample,name,dest))
        with (fold/'manifest.csv').open('w',newline='',encoding='utf8') as f:
            w=csv.writer(f)
            w.writerow(['dataset','heldout_sample','validation_sample','split','sample','original_filename','fold_filename'])
            w.writerows(manifest)
        counts={split:sum(row[3]==split for row in manifest) for split in ('train','val','test')}
        print(f'{ds:6} test={holdout:10} val={val:10} train={counts["train"]:4} val={counts["val"]:4} test={counts["test"]:4} -> {fold}')
        return fold
    except Exception:
        # Remove only newly created incomplete fold.
        shutil.rmtree(fold)
        raise

def main():
    p=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--root',type=Path,default=DEFAULT_ROOT)
    p.add_argument('--output',type=Path,default=None)
    p.add_argument('--dataset',choices=list(SAMPLES))
    p.add_argument('--test-sample')
    p.add_argument('--all',action='store_true')
    p.add_argument('--list',action='store_true')
    p.add_argument('--link-mode',choices=['copy','hardlink','symlink'],default='copy')
    args=p.parse_args()
    if args.list:
        for ds,samples in SAMPLES.items():
            print(ds,':',', '.join(samples))
        return
    if not args.all and not (args.dataset and args.test_sample):
        p.error('Use --all or --dataset DATASET --test-sample SAMPLE')
    if args.all and (args.dataset or args.test_sample):
        p.error('Use --all alone, or choose one fold')
    root=args.root
    output=args.output or root.parent/'pix2pix_LOSO'
    jobs=[(ds,s) for ds in SAMPLES for s in SAMPLES[ds]] if args.all else [(args.dataset,args.test_sample)]
    for ds,s in jobs:
        build_one(root,output,ds,s,args.link_mode)
    print('Complete. No train/validation crop comes from each fold\'s held-out test sample.')

if __name__=='__main__':
    main()
