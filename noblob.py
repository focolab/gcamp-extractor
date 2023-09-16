#!/usr/bin/env python3
## Example use case of eats-worm package

from eats_worm import *

## pixelSize = [0.35, 0.75, 0.3545×sin(π×Θ°/180°)]
<<<<<<< Updated upstream
#m = MultiFileTiff('E:/SCAPE/Data/tiff_stacks/20230913_OH16290_1_run2/Deskewed_-45', numz=200, numc=1, anisotropy=(0.55, 1, 0.47))
#m = MultiFileTiff('E:/SCAPE/Data/HiCAM_2000/165mm/NeuroPAL/20230914/tiff_stacks/20230914_OH16290_3_run1/Deskewed_-45', numz=200, numc=1, anisotropy=(0.55, 0.5, 0.47))
m = MultiFileTiff('E:/SCAPE/Data/HiCAM_2000/165mm/GreenBeads/tiff_stacks/runA_run1/09-15-15-54', numz=200, numc=1, anisotropy=(1, 0.55, 0.47))
=======
#m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/HiCAM_2000/165mm/GreenBeads/20230911_GreenBeads4um_run3', numz=200, numc=1, anisotropy=(0.55, 1, 0.47))
m = MultiFileTiff('Z:/muneki/MATLAB/SCAPE/Data/HiCAM_2000/165mm/NeuroPAL/20230913_OH16290_2_run1/Deskewed_-45', numz=200, numc=1, anisotropy=(0.55, 1, 0.47))
>>>>>>> Stashed changes

viewer = napari.Viewer(ndisplay=3)
viewer.add_image(m.get_dask_array(), scale=m.anisotropy)
napari.run()