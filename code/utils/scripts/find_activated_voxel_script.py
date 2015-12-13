from __future__ import division, print_function, absolute_import
import numpy as np
import sys
sys.path.append(".././utils")
import nibabel as nib
import matplotlib.pyplot as plt
from load_BOLD import *
from t_test import *
from find_activated_voxel_functions import *
from convolution_normal_script import X_matrix
from convolution_high_res_script import X_matrix_high_res

location_of_data = "../../data/ds005/sub001/BOLD/task001_run001/"
data = load_img(1,1)
beta, t, df,p=t_test(data,X_matrix_high_res)
shape = data.shape[:3]

position1,position2, position3,position4 = find_activated_voxel(shape, p)
location_of_txt="../txt_files/"
np.savetxt(location_of_txt+'ds005_sub001_t1r1_position1.txt',position1,fmt='%i')
np.savetxt(location_of_txt+'ds005_sub001_t1r1_position2.txt',position2,fmt='%i')
np.savetxt(location_of_txt+'ds005_sub001_t1r1_position3.txt',position3,fmt='%i')
np.savetxt(location_of_txt+'ds005_sub001_t1r1_position4.txt',position4,fmt='%i')
