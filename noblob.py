#!/usr/bin/env python3
## Example use case of eats-worm package

from eats_worm import *

## pixelSize = [0.35, 0.75, 0.3545×sin(π×Θ°/180°)]
#m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/Voleti_et_al_Nat_Meth_2019/Immobilized_actual_properScale/green_actual_properScale', numz=157, numc=1, anisotropy=(0.20, 76.5/383, 103/532)) #anisotropy=(0.20, 0.75, 0.24))
#m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/Voleti_et_al_Nat_Meth_2019/Moving_actual_properScale/green_actual_properScale', numz=127, numc=1, anisotropy=(0.32, 229/716, 392/1217)) #anisotropy=(0.32, 1.42, 0.37))
#m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/PythonScripts/wormjam/rawdata/worm02_act1/GCAMP', numz=12, numc=1, anisotropy=(3, 0.22, 0.22))
m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/Zyla_4.2PLUS/165mm/GreenBeads/tiff_stacks', numz=802, numc=1, anisotropy=[0.25, 1, 0.35])
#m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/Zyla/165mm/NeuroPAL/20230716_OH16290_1_run1', numz=127, numc=1, anisotropy=(0.25, 0.75, 0.35))
#m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/HiCAM_2000/165mm/GreenBeads/20230911_GreenBeads4um_run3/Deskewed_-60', numz=200, numc=1, anisotropy=(0.47, 1, 0.55))
#m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/HiCAM_2000/165mm/NeuroPAL/20230916_OH16290_2_run1/Deskewed_-45', numz=200, numc=1, anisotropy=(0.39, 1, 0.55))
#m = MultiFileTiff('C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/HiCAM_2000/165mm/NeuroPAL/20230928_OH16290_1_run1/Deskewed_-40', numz=200, numc=1, anisotropy=(0.35, 1, 0.55))

viewer = napari.Viewer(ndisplay=3)
viewer.add_image(m.get_dask_array(), scale=m.anisotropy)
napari.run()