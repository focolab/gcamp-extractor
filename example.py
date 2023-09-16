#!/usr/bin/env python3
## Example use case of eats-worm package

from eats_worm import *

<<<<<<< Updated upstream
#data_directory = "D:/SCAPE/Data/Voleti_et_al_Nat_Meth_2019/Immobilized_actual_properScale/green_actual_properScale"; numZ = 157; endT = 2; pixelSize = [0.75, 0.24, 0.20]
#data_directory = "D:/SCAPE/Data/Voleti_et_al_Nat_Meth_2019/Moving_actual_properScale/green_actual_properScale"; numZ = 127; endT = 10; pixelSize = [1.42, 0.37, 0.32]
## pixelSize = [0.35, 0.75, 0.3545×sin(π×Θ°/180°)]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230724_OH16290_1_run1"; numZ = 120; endT = 1715; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "E:/SCAPE/Data/tiff_stacks/20230908_GreenBeads4um_run2/20230908_GreenBeads4um_run2"; numZ = 200; endT = 3; pixelSize = [1.8, 1, 1.16]
#data_directory = "E:/SCAPE/Data/20230911/tiff_stacks/20230911_GreenBeads4um_run3/Deskewed_-60"; numZ = 200; endT = 3; pixelSize = [0.55, 1, 0.47]
data_directory = "E:/SCAPE/Data/HiCAM_2000/165mm/NeuroPAL/20230913/tiff_stacks/20230913_OH16290_3_run1/Deskewed_-45"; numZ = 200; endT = 10; pixelSize = (0.55, 1, 0.47)
=======
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/Voleti_et_al_Nat_Meth_2019/Immobilized_actual_properScale/green_actual_properScale"; numZ = 157; endT = 360; pixelSize = [0.75, 0.24, 0.20]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/Voleti_et_al_Nat_Meth_2019/Moving_actual_properScale/green_actual_properScale"; numZ = 127; endT = 100; pixelSize = [1.42, 0.37, 0.32]
#data_directory = "Z:/muneki/MATLAB/SCAPE/Data/Voleti_et_al_Nat_Meth_2019/Immobilized_actual_properScale/green_actual_properScale"; numZ = 157; endT = 3575; pixelSize = [0.75, 0.24, 0.20]
## pixelSize = [0.35, 0.75, 0.3545×sin(π×Θ°/180°)]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230522_OH16290_1_run2"; numZ = 199; endT = 1039; pixelSize = [0.35, 0.75, 0.29]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230529_OH16290_1_run1"; numZ = 127; endT = 1039; pixelSize = [0.35, 0.75, 0.29]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230529_OH16290_2_run1"; numZ = 127; endT = 985; pixelSize = [0.35, 0.75, 0.29]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230711_OH16290_1_run1"; numZ = 127; endT = 1688; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230714_OH16290_1_run1"; numZ = 127; endT = 1685; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230715_OH16290_1_run1"; numZ = 127; endT = 1684; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230716_OH16290_1_run1"; numZ = 127; endT = 1682; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230719_OH16290_1_run1"; numZ = 120; endT = ; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230720_OH16290_1_run1"; numZ = 120; endT = 1714; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230721_OH16290_1_run1"; numZ = 120; endT = 1713; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230722_OH16290_1_run1"; numZ = 120; endT = 1712; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230723_OH16290_1_run1"; numZ = 120; endT = 1715; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230723_OH16290_1_run2"; numZ = 120; endT = 1715; pixelSize = [0.35, 0.75, 0.25]
#data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230724_OH16290_1_run1"; numZ = 120; endT = 1715; pixelSize = [0.35, 0.75, 0.25]
data_directory = "C:/Users/miked/OneDrive - UCSF/Documents/MATLAB/SCAPE/Data/165mm/NeuroPAL/tiff_stacks/20230726_OH16290_1_run2"; numZ = 120; endT = 1715; pixelSize = [0.35, 0.75, 0.25]
>>>>>>> Stashed changes
output_directory = data_directory + "/output/"


arguments = {
    "root": data_directory,
    "numz": numZ,
    #"frames":[1,2,3,4,5,6,7,8,9,10,11],
    "numc": 1,
    "end_t": endT,
    "offset": 0,
    "gaussian": False,
    "median": 3, #5
    "quantile": 0.963, #0.999
    "anisotropy": pixelSize,
    "blob_merge_dist_thresh": 5, #10
    "remove_blobs_dist": 3,
    "algorithm":"tmip_2d_template",
    "algorithm_params": {
        "window_size": 5, #3
        "min_distance": 11, #1
        "manage_collisions": "prune",
<<<<<<< Updated upstream
        "fb_threshold_margin": 50 #10
    },
    "register_frames": False, #True
=======
        "fb_threshold_margin": 50
    },
    "register_frames": True,
>>>>>>> Stashed changes
    "output_dir": output_directory
}

e = Extractor(**arguments)

e.calc_blob_threads()
e.quantify(quant_function=background_subtraction_quant_function)

#e = load_extractor(output_directory)

c = Curator(e=e)