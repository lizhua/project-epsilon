"""
ADD DESCRIPTION
"""

import sys, os
sys.path.append("../utils")
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import matplotlib

from t_test import *
from find_activated_voxel_functions import *
from convolution_normal_script import X_matrix
from scipy.ndimage import gaussian_filter
from matplotlib import colors
=======
Purpose:
-----------------------------------------------------------
This script creates graphs for t-test for 4 conditions
For each subject each run each condition, plot the t statistics
-----------------------------------------------------------

"""
import sys, os
sys.path.append("../utils")

from t_test import *
from find_activated_voxel_functions import *
from smoothing import *
from matplotlib import colors
from visualization import *

import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import matplotlib
>>>>>>> ff6f30e3cd78e9ab34688663f9ba2b59a15b1bf2

# Create the necessary directories if they do not exist
dirs = ['../../fig','../../fig/t-test']
for d in dirs:
    if not os.path.exists(d):
        os.makedirs(d)

# Locate the different paths
project_path = '../../'
data_path = project_path + 'data/ds005/'
txt_path = project_path + 'txt_output/conv_normal/'

# TODO: uncomment for final version
#subject_list = [str(i) for i in range(1,17)]
subject_list = ['1','5','11']
run_list = [str(i) for i in range(1,4)]
cond_list = [str(i) for i in range(1,5)]

#TODO: Change to relevant path for data or other thing
images_paths = [('ds005_sub' + s.zfill(3) + '_t1r' + r, \
                 data_path + 'sub' + s.zfill(3) + '/BOLD/task001_run' \
                 + r.zfill(3) + '/bold.nii.gz') for r in run_list \
                 for s in subject_list]


for image_path in images_paths:
    name = image_path[0]
    img = nib.load(image_path[1])
    data = img.get_data()
    vol_shape = data.shape[:-1]
    #get the mean value
    mean_data = np.mean(data, axis = -1)
    #build the mask
    in_brain_mask = mean_data > 375
    #smooth the data set
    smooth_data = smoothing(data, 1, range(data.shape[-1]))
    #initialize design matrix for t test
    X_matrix = np.ones((data.shape[-1],5))
    #build our design matrix
    for cond in range(1,5):
	convolved = np.loadtxt(txt_path + name + '_conv_' + str(cond).zfill(3) + '_canonical.txt')
        X_matrix[:,cond] = convolved
    beta, t, df, p = t_test(smooth_data, X_matrix)
    for cond in range(0,4):
        beta_newshape = np.reshape(beta[:,cond],vol_shape)
        beta_newshape[~in_brain_mask]=np.nan
        beta_T = np.zeros(vol_shape)
        for z in range(vol_shape[2]):
            beta_T[:, :, z] = beta_newshape[:,:, z].T
        beta_plot = present_3d(beta_T)
        plt.imshow(beta_plot,interpolation='nearest', cmap='seismic')
        zero_out=max(abs(np.nanmin(beta_T)),np.nanmax(beta_T))
        plt.title(name+'_beta_hat'+'_cond_'+'_%s'%(cond+1))
        plt.clim(-zero_out,zero_out)
        plt.colorbar()
        plt.savefig(dirs[1]+'/'+ name +'_t-test_'+'cond'+str(cond+1)+'.png')
        plt.close()

#t2 = np.reshape(t[2,:], vol_shape)
#n_vol = np.mean(data, axis=-1)t2[~in_brain_mask]=np.nan
#for i in range(34):
# plt.subplot(5,7,i+1)
# plt.imshow(t2[:,:,i])
# plt.title("Slice"+str(i+1), fontsize=5)
# plt.tight_layout()

#plt.suptitle("Subject 1 Run 1 T Statistics in Condition 2 for different Slices\n")
#plt.colorbar()
#plt.savefig(location_of_plot+"t_statistics_for_condition_2")
#plt.close()

#t3 = np.reshape(t[3,:],vol_shape)
#t3[~in_brain_mask]=np.nan
#for i in range(34):
 #plt.subplot(5,7,i+1)
# plt.imshow(t3[:,:,i])
 #plt.title("Slice"+str(i+1), fontsize=5)
# plt.tight_layout()

#plt.suptitle("Subject 1 Run 1 T Statistics in Condition 3 for different Slices\n")
#plt.colorbar()
#plt.savefig(location_of_plot+"t_statistics_for_condition_3")
#plt.close()

#t4 = np.reshape(t[4,:],vol_shape)
#t4[~in_brain_mask]=np.nan
#for i in range(34):
# plt.subplot(5,7,i+1)
# plt.imshow(t4[:,:,i])
# plt.title("Slice"+str(i+1), fontsize=5)
# plt.tight_layout()

<<<<<<< HEAD
# Create the necessary directories if they do not exist
dirs = ['../../txt_output', '../../txt_output/FOLDERS_NAME',\
        '../../fig','../../fig/FOLDER_NAME']
for d in dirs:
    if not os.path.exists(d):
        os.makedirs(d)

# Locate the different paths
project_path = '../../'
data_path = project_path + 'data/ds005/'

# TODO: uncomment for final version
#subject_list = [str(i) for i in range(1,17)]
subject_list = ['1']
run_list = [str(i) for i in range(1,2)]

#TODO: Change to relevant path for data or other thing
images_paths = [('ds005_sub' + s.zfill(3) + '_t1r' + r, \
                 dir_path + 'sub' + s.zfill(3) + '/BOLD/task001_run' \
                 + r.zfill(3) + '/bold.nii.gz') for r in run_list \
                 for s in subject_list]

#TODO: remove the following
location_of_data = "../../data/ds005/sub001/BOLD/task001_run001/"
location_of_plot = "../../plots/"


#TODO:See the script hist-mosaic for plot

img = nib.load(location_of_data+ "bold.nii")
data = img.get_data()
data = data[4:,]
smooth_data = gaussian_filter(data, [2, 2, 2, 0])
beta, t, df,p=t_test(smooth_data,X_matrix)
vol_shape, n_trs = data.shape[:-1], data.shape[-1]

#find mask boolean vectors
mean_data = np.mean(data,axis=-1)
in_brain_mask = mean_data > 400

#nice map
nice_cmap_values = np.loadtxt('actc.txt')
nice_cmap = colors.ListedColormap(nice_cmap_values, 'actc')

#set up the label font size
matplotlib.rc('xtick', labelsize=5) 
matplotlib.rc('ytick', labelsize=5) 

#draw heat map
t1 = np.reshape(t[1,:],vol_shape)
t1[~in_brain_mask]=np.nan
for i in range(34):
 plt.subplot(5,7,i+1)
 plt.imshow(t1[:,:,i],cmap = nice_cmap, alpha=0.5)
 plt.title("Slice"+str(i+1), fontsize=5)
 plt.tight_layout()

plt.suptitle("Subject 1 Run 1 T Statistics in Condition 1 for different Slices\n")
plt.colorbar()
plt.savefig(location_of_plot+"t_statistics_for_condition_1")
plt.close()

t2 = np.reshape(t[2,:], vol_shape)
t2[~in_brain_mask]=np.nan
for i in range(34):
 plt.subplot(5,7,i+1)
 plt.imshow(t2[:,:,i])
 plt.title("Slice"+str(i+1), fontsize=5)
 plt.tight_layout()

plt.suptitle("Subject 1 Run 1 T Statistics in Condition 2 for different Slices\n")
plt.colorbar()
plt.savefig(location_of_plot+"t_statistics_for_condition_2")
plt.close()

t3 = np.reshape(t[3,:],vol_shape)
t3[~in_brain_mask]=np.nan
for i in range(34):
 plt.subplot(5,7,i+1)
 plt.imshow(t3[:,:,i])
 plt.title("Slice"+str(i+1), fontsize=5)
 plt.tight_layout()

plt.suptitle("Subject 1 Run 1 T Statistics in Condition 3 for different Slices\n")
plt.colorbar()
plt.savefig(location_of_plot+"t_statistics_for_condition_3")
plt.close()

t4 = np.reshape(t[4,:],vol_shape)
t4[~in_brain_mask]=np.nan
for i in range(34):
 plt.subplot(5,7,i+1)
 plt.imshow(t4[:,:,i])
 plt.title("Slice"+str(i+1), fontsize=5)
 plt.tight_layout()

plt.suptitle("Subject 1 Run 1 T Statistics in Condition 4 for different Slices\n")
plt.colorbar()
plt.savefig(location_of_plot+"t_statistics_for_condition_4")
plt.close()
=======
#plt.suptitle("Subject 1 Run 1 T Statistics in Condition 4 for different Slices\n")
#plt.colorbar()
#plt.savefig(location_of_plot+"t_statistics_for_condition_4")
#plt.close()
>>>>>>> ff6f30e3cd78e9ab34688663f9ba2b59a15b1bf2

