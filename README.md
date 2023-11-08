# kmeans-beamtilt
Beam tilt refinement by image shift groups in cryoSPARC for datasets acquired with the Leginon & Appion suite.  

kmeans_groups.py
- reads the input.csv file to group the micrographs based on their image shift groups.  
- Usage: kmeans_groups.py k inputcsv
- outputs numbered km_groups.csv, km_centers.csv, and km_plot.png files.  

add_class.sh
- adds 3 digit class numbers to the symlinked micrographs.
- Usage: add_class.sh -d DIRECTORY -i FILE

assign_kmeans_exp_groups_pub.ipynb
- a Jupyter notebook to directly assign the exposure group IDs calculated by kmeans_group.py via cryosparc-tools (https://tools.cryosparc.com/intro.html)

K-means script by Bill Rice (https://github.com/wjrice/tiltgroup_wrangler)  
You can find the step by step guide in the repository wiki (https://github.com/kookjookeem/kmeans-beamtilt/wiki).  
