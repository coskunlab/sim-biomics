# SIM-BIOMICS

### Overview and Repository Structure
This repository contains the notebooks to produce results from the paper "Spatial renal biomarker discovery using multiplexed immunofluorescent and high-dimensional colorimetric staining."

### Usage 


### Examples  
Notebooks in folder 01_image_processing align images of the same tissue across stains:  

<img width="1141" height="1521" alt="image" src="https://github.com/user-attachments/assets/a3a9513a-0fe5-416c-a374-c3c6983dd37a" />

Notebooks in folder 02_cell_phenotyping segment and phenotype cells based on detected markers and compute the fraction of cell populations within the tissue:

<img width="481" height="134" alt="image" src="https://github.com/user-attachments/assets/df13cde7-ed28-4f1d-9e0d-f0c0ecf714b8" />
<img width="210" height="225" alt="image" src="https://github.com/user-attachments/assets/ce492779-ddaa-4f7f-97b7-6e240d3012a8" />

Notebooks in folder 03_pixel_clustering applies pixel clustering to a tissue to integrate information from multiplexed immunofluorescent and histological stains. Computational efficiency of PARC and SOM clustering can be compared for a sample using `compare_pixel_clustering_algorithm_run_times.ipynb`. Following SOM clustering, the pixel clusters are visualized in regions of interest and the fraction of pixels assigned to each cluster quantified using `visualize_cluster_distribution_across_wsi.ipynb`. The average intensity and/or hue of fluorescent markers and histological stains for each cluster is visualized through `visualize_pixel_clustering_heatmap.ipynb`. The likelihood of clusters neighboring each other can be quantified and visualized through `compute_probability_cluster_neighbors.ipynb`.
<img width="1095" height="1460" alt="image" src="https://github.com/user-attachments/assets/2a0fc6ff-746d-402d-afb0-081e20b7515c" />








