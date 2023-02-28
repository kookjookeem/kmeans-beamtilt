# kmeans-beamtilt
Beam tilt refinement by image shift groups in cryoSPARC for datasets acquired by the Leginon & Appion suite  

kmeans_groups.py reads the pre-prepared csv file with micrograph name and imageshift X & Y to group the micrographs based on their image shift groups.  

The python script outputs numbered km_groups.csv, km_centers.csv, and km_plot.png files.  
add_class.sh adds class identifier numbers to the symlinked micrographs.

You can find the step by step guide in the repository wiki (https://github.com/kookjookeem/kmeans-beamtilt/wiki).  
