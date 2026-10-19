# SIM-BIOMICS

### Overview and Repository Structure
This repository contains the notebooks to produce results from the paper "Spatial renal biomarker discovery using multiplexed immunofluorescent and high-dimensional colorimetric staining."

### Usage 


### Examples  
Notebooks in folder 01_image_processing align images of the same tissue across stains:  

<img width="1141" height="1521" alt="image" src="https://github.com/user-attachments/assets/a3a9513a-0fe5-416c-a374-c3c6983dd37a" />

Notebooks in folder 02_cell_phenotyping segment and phenotype cells based on detected markers and compute the fraction of cell populations within the tissue:

<img width="481" height="134" alt="image" src="https://github.com/user-attachments/assets/df13cde7-ed28-4f1d-9e0d-f0c0ecf714b8" />

Notebooks in folder 03_pixel_clustering applies pixel clustering to a tissue to integrate information from multiplexed immunofluorescent and histological stains. Computational efficiency of PARC and SOM clustering can be compared for a sample using `compare_pixel_clustering_algorithm_run_times.ipynb`. Following SOM clustering, the pixel clusters are visualized in regions of interest and the fraction of pixels assigned to each cluster quantified using `visualize_cluster_distribution_across_wsi.ipynb`. The average intensity and/or hue of fluorescent markers and histological stains for each cluster is visualized through `visualize_pixel_clustering_heatmap.ipynb`. The likelihood of clusters neighboring each other can be quantified and visualized through `compute_probability_cluster_neighbors.ipynb`.
<img width="1095" height="1460" alt="image" src="https://github.com/user-attachments/assets/2a0fc6ff-746d-402d-afb0-081e20b7515c" />

Notebooks in folder 04_inflammatory_spatial_niches can be used to barcode each immune cell based on its environment and identify cell subtypes. 

<img width="1125" height="1500" alt="image" src="https://github.com/user-attachments/assets/d255478e-76d9-4b05-8f6b-9dc195b1a9f3" />

Notebooks in folder 05_glomerulosclerosis detection can be used for comparison and classification of globally sclerotic and non-globally sclerotic glomeruli. Glomeruli are barcoded based using `create_glomerulus_pixel_barcodes.ipynb`. A model is trained and evaluated for glomerulosclerosis detection using `predict_globally_sclerotic_glomeruli.ipynb`. 

<img width="1028" height="393" alt="image" src="https://github.com/user-attachments/assets/d0af04c3-c54e-4a00-9477-7d92ac7144af" />


PAS and Trichrome features are compared between globally sclerotic and non globally sclerotic glomeruli using `compare_cell_density_fibrosis_between_sclerotic_non_sclerotic_glomeruli.ipynb`.

<img width="819" height="641" alt="image" src="https://github.com/user-attachments/assets/a81d737a-658e-47f1-b0df-6a0544ee725a" />

Notebooks in folder 06_mapping fibrosis can be used for detecting fibrosis subtypes in a tissue and identifying cell populations involved in fibrosis. 

`segment_fibrosis_edema_inflammation.ipynb` can be used to segment i-IFTA, established fibrosis and diffuse fibrosis in a tissue and produce a fibrosis segmentation map. 

<img width="384" height="341" alt="image" src="https://github.com/user-attachments/assets/b36f87ae-5a2a-4d99-8407-aae7b0486e4b" />

`compute_fibrosis_distribution_across_wsi.ipynb` can be used to compute the proportion of different fibrosis subtypes per tile across the tissue 

<img width="444" height="227" alt="image" src="https://github.com/user-attachments/assets/2a1870e3-6ec2-4966-9ec8-a314a22d80f2" />

`overlay_cell_type_on_fibrosis_cluster_map.ipynb` can be used to overlay the cell segmentation mask color coded by cell phenotype on the fibrosis segmentation map. 

<img width="358" height="357" alt="image" src="https://github.com/user-attachments/assets/9e463c51-533e-468b-acc3-c31d1bd2550d" />

`project_cell_protein_fibrosis_barcodes.ipynb` can be used to create and project cells based on cell-protein barcodes, cell-fibrosis barcodes or cell-protein-fibrosis barcodes. 

### Environments
The env folder contains requirements.txt file for the five main environments used with this pipeline:
stitch_subtract_af  
- stitch_subtract_af 

registration 
- compare registration_algorithms 
- register_interstitium_mask 

cell_phenotyping 
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
- fibrosis_barycentric_projection
- compare_real_virtual_stain_quality
- project_cell_protein_fibrosis_barcodes 

napari 
- overlay_cell_type_on_fibrosis_clustermap 

pixel_clustering_som 
- compare_pixel_clustering_algorithm_run_time
- compute_optimal_som_cluster_number
- pixel_clustering_som 
- segment_fibrosis_edema_inflammation.ipynb 

color_deconvolution  
- color_deconvolution 
- quantify_color_image_bleaching 










