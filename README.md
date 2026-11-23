# SIM-BIOMICS

### Overview and Repository Structure
This repository contains the notebooks to produce results from the paper "Spatial renal biomarker discovery using multiplexed immunofluorescent and high-dimensional colorimetric staining."

### Usage 
Operating System: Tested on Windows 11 (64-bit)\
GPU: NVIDIA CUDA-enabled	recommended for DeepCell performance

### Examples  
Notebooks in folder 01_image_processing align images of the same tissue across stains:  

<img width="1141" height="1521" alt="image" src="https://github.com/user-attachments/assets/a3a9513a-0fe5-416c-a374-c3c6983dd37a" />

Notebooks in folder 02_cell_phenotyping segment and phenotype cells based on detected markers and compute the fraction of cell populations within the tissue:

<img width="481" height="134" alt="image" src="https://github.com/user-attachments/assets/df13cde7-ed28-4f1d-9e0d-f0c0ecf714b8" />

Notebooks in folder 03_pixel_clustering applies pixel clustering to a tissue to integrate information from multiplexed immunofluorescent and histological stains. Computational efficiency of PARC and SOM clustering can be compared for a sample using `compare_pixel_clustering_algorithm_run_times.ipynb`. Following SOM clustering, the pixel clusters are visualized in regions of interest and the fraction of pixels assigned to each cluster quantified using `visualize_cluster_distribution_across_wsi.ipynb`. The average intensity and/or hue of fluorescent markers and histological stains for each cluster is visualized through `visualize_pixel_clustering_heatmap.ipynb`. The likelihood of clusters neighboring each other can be quantified and visualized through `compute_probability_cluster_neighbors.ipynb`.
<img width="1095" height="1460" alt="image" src="https://github.com/user-attachments/assets/2a0fc6ff-746d-402d-afb0-081e20b7515c" />

Notebooks in folder 04_inflammatory_spatial_niches can be used to barcode each immune cell based on its environment and identify cell subtypes. 

<img width="900" height="1200" alt="image" src="https://github.com/user-attachments/assets/653058eb-52b1-451a-be14-6c934aea77d8" />


Notebooks in folder 05_glomerulosclerosis detection can be used for comparison and classification of globally sclerotic and non-globally sclerotic glomeruli. Glomeruli are barcoded based using `create_glomerulus_pixel_barcodes.ipynb`. A model is trained and evaluated for glomerulosclerosis detection using `predict_globally_sclerotic_glomeruli.ipynb`. 

<img width="1028" height="393" alt="image" src="https://github.com/user-attachments/assets/d0af04c3-c54e-4a00-9477-7d92ac7144af" />


PAS and Trichrome features are compared between globally sclerotic and non globally sclerotic glomeruli using `compare_cell_density_fibrosis_between_sclerotic_non_sclerotic_glomeruli.ipynb`.

<img width="834" height="651" alt="image" src="https://github.com/user-attachments/assets/235d2db8-3167-470e-8ef0-bd988fe0ec14" />

Notebooks in folder 06_mapping fibrosis can be used for detecting fibrosis subtypes in a tissue and identifying cell populations involved in fibrosis. 

`segment_fibrosis_edema_inflammation.ipynb` can be used to segment i-IFTA, established fibrosis and diffuse fibrosis in a tissue and produce a fibrosis segmentation map. 
<img width="224" height="410" alt="image" src="https://github.com/user-attachments/assets/26225904-5a6a-4c5a-92a0-a78090b035cd" />



`compute_fibrosis_distribution_across_wsi.ipynb` can be used to compute the proportion of different fibrosis subtypes per tile across the tissue 

<img width="438" height="242" alt="image" src="https://github.com/user-attachments/assets/fe4dd3ec-150d-4790-af15-468a917b5681" />



`overlay_cell_type_on_fibrosis_cluster_map.ipynb` can be used to overlay the cell segmentation mask color coded by cell phenotype on the fibrosis segmentation map. 

<img width="296" height="293" alt="image" src="https://github.com/user-attachments/assets/9d2c0c41-8b09-4ecc-b4c0-15281c13c7ff" />


`project_cell_protein_fibrosis_barcodes.ipynb` can be used to create and project cells based on cell-protein barcodes, cell-fibrosis barcodes or cell-protein-fibrosis barcodes. 

### Environments
The env folder contains requirements.txt file for the five main environments used with this pipeline:

stitch_subtract_af (Python 3.13.2)
- stitch_subtract_af\
To create this environment:\
`conda create -n stitch_subtract_af_venv python=3.13.2`\
`pip install numpy tqdm datetime joblib tifffile pathlib opencv-python scikit-image dask`

registration (Python 3.13.2)
- compare registration_algorithms 
- register_interstitium_mask\
To create this environment:\
`conda create -n registration_venv python=3.13.2`\
`pip install pathlib opencv-python dask tifffile numpy scikit-image matplotlib tqdm`

cell_phenotyping_venv (Python 3.10.19)
- compute_registration_quality
- quantify_background
- quantify_IF_image_bleaching
- quantify_tissue_distortion_due_to_multiplexing
- visualize_color_stain_regions
- cell_segmentation_clustering
- cell_segmentation_for_registration_quality
- generate_cell_expression_phenotype_statistics
- compute_channel_contributions_to_pixel_clusters
- compute_probability_cluster_neighbors
- quantify_cluster_concordance
- visualize_cluster_distribution_across_wsi
- visualize_pixel_clustering_heatmap
- All notebooks in 04_inflammatory_spatial_niches
- All notebooks in 05_glomerulosclerosis_detection except color_deconvolution
- compute_fibrosis_distribution_across_wsi
- compare_real_virtual_stain_quality
- project_cell_protein_fibrosis_barcodes

To create this environment:\
`conda create -n cell_phenotyping_venv python=3.10.19`\
`pip install deepcell`\
`pip install opencv-python==4.11.0.86`\
`pip install scanpy==1.10.2`\
`pip install pandas scikit-image imagecodecs tifffile matplotlib scipy distinctipy pathlib pyarrow dask scikit-image tqdm igraph leidenalg statannotations matplotlib-scalebar umap-learn tqdm-joblib joblib imblearn statistics`

virtual_staining_evaluation_venv (Python 3.10.19)
- compare_real_virtual_stain_quality.ipynb\
To create this environment:\
`conda create -n virtual_staining_evaluation_venv python=3.10.19`\
`conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1  pytorch-cuda=11.8 -c pytorch -c nvidia`\
`pip install lpips pathlib scikit-image matplotlib pytorch_msssim tqdm`

napari_venv (Python 3.10.19)
- overlay_cell_type_on_fibrosis_clustermap
- fibrosis_barycentric_projection\
  
napari 0.7 must be installed\
To create this environment:\
`conda create -n napari_venv python=3.10.19`\
`python -m pip install "napari[all]<0.8.0"`\
`pip install opencv-python==4.11.0.86`\
`pip install tifffile matplotlib pathlib pandas tqdm scikit-image scipy distinctipy`


pixel_clustering_som (Python 3.11.11)
- compare_pixel_clustering_algorithm_run_time
- compute_optimal_som_cluster_number
- pixel_clustering_som 
- segment_fibrosis_edema_inflammation.ipynb\
  
To create this environment:\
`conda create -n pixel_clustering_som_venv python=3.11.11`\
`pip install pyFlowSOM pathlib tifffile pandas scikit-learn scipy matplotlib-scalebar matplotlib alpineer pyarrow parc  tqdm tqdm-joblib joblib seaborn opencv-python distinctipy`

color_deconvolution (Python 3.13.5)
- color_deconvolution 
- quantify_color_image_bleaching

To create this environment:\
`conda create -n color_deconvolution_venv python=3.13.5`\
Follow instructions for libvips installation: https://www.libvips.org/install.html\
`pip install pyvips`\
`conda install -c conda-forge large-image`\
`conda install -c conda-forge large-image-source-gdal`\
`conda install -c conda-forge large-image-source-tiff`\
`pip install large-image-converter[sources] --find-links https://girder.github.io/large_image_wheels`\
`pip install cmake`\
`pip install pylibtiff`\
`git clone https://github.com/DigitalSlideArchive/HistomicsTK.git`\
`cd HistomicsTK`\
`python -m pip install setuptools-scm "Cython>=0.25.2" "scikit-build>=0.8.1" "cmake>=0.6.0" "numpy>=1.12.1"`\
p`ython -m pip install -e .`\
`pip install pathlib tifffile matplotlib`

virtual_staining 
- All virtual staining notebooks except compare_real_virtual_stain_quality
Create environment from requirements.txt file










