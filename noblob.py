#!/usr/bin/env python3
## Example use case of eats-worm package

from eats_worm import *

## pixelSize = [0.35, 0.75, 0.3545×sin(π×Θ°/180°)]
#m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/HiCAM_2000/165mm/GreenBeads/20230911_GreenBeads4um_run3', numz=200, numc=1, anisotropy=(0.55, 1, 0.47))
m = MultiFileTiff('Z:/muneki/MATLAB/SCAPE/Data/HiCAM_2000/165mm/NeuroPAL/20230913_OH16290_2_run1/Deskewed_-45', numz=200, numc=1, anisotropy=(0.55, 1, 0.47))

viewer = napari.Viewer(ndisplay=3)
viewer.add_image(m.get_dask_array(), scale=m.anisotropy)
napari.run()