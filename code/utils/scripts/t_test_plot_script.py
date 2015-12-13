"""
Purpose:
-----------------------------------------------------------
This script creates graphs for t-test for 4 conditions
For each subject each run each condition, plot the t statistics
-----------------------------------------------------------

"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))

from t_test import *
from smoothing import *
from matplotlib import colors
from visualization import *

import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import matplotlib

# Create the necessary directories if they do not exist
dirs = ['../../../fig','../../../fig/t-test']
for d in dirs:
    if not os.path.exists(d):
        os.makedirs(d)

# Locate the different paths
project_path = '../../../'
data_path = project_path + 'data/ds005/'
txt_path = project_path + 'txt_output/conv_high_res/'
#txt_path = project_path + 'txt_output/conv_normal/'
path_dict = {'data_filtered':{ 
			      'type' : 'filtered',
			      'bold_img_name' : 'filtered_func_data_mni.nii.gz',
			      'run_path' : 'model/model001/'
			     },
             'data_original':{
		       	      'type' : '',
                              'bold_img_name' : 'bold.nii.gz',
                              'run_path' : 'BOLD/'
			     }}

# TODO: uncomment for final version
#subject_list = [str(i) for i in range(1,17)]
subject_list = ['1','5','11']
run_list = [str(i) for i in range(1,4)]
cond_list = [str(i) for i in range(1,5)]

#TODO: Change to relevant path for data or other thing
d = path_dict['data_original'] #OR path_dict['data_filtered']
images_paths = [('ds005' + d['type'] +'_sub' + s.zfill(3) + '_t1r' + r, \
                 data_path + 'sub%s/'%(s.zfill(3)) + d['run_path'] \
                 + 'task001_run%s/%s' %(r.zfill(3), d['bold_img_name'])) \
                 for r in run_list \
                 for s in subject_list]

thres = 375 #from analysis of the histograms
for image_path in images_paths:
    name = image_path[0]
    img = nib.load(image_path[1])
    data = img.get_data()
    vol_shape = data.shape[:-1]
    n_trs = data.shape[-1]
    #get the mean value
    mean_data = np.mean(data, axis = -1)
    #build the mask
    in_brain_mask = mean_data > 375
    #smooth the data set
    smooth_data = smoothing(data, 1, range(n_trs))
    #initialize design matrix for t test
    p = 7
    X_matrix = np.ones((data.shape[-1], p))
    #build our design matrix
    for cond in range(1,5):
        convolved = np.loadtxt(txt_path + name + '_conv_' + str(cond).zfill(3) + '_high_res.txt')
	#convolved = np.loadtxt(txt_path + name + '_conv_' + str(cond).zfill(3) + '_canonical.txt')
        X_matrix[:,cond] = convolved
    linear_drift = np.linspace(-1, 1, n_trs)
    X_matrix[:,5] = linear_drift
    quadratic_drift = linear_drift ** 2
    quadratic_drift -= np.mean(quadratic_drift)
    X_matrix[:,6] = quadratic_drift
    beta, t, df, p = t_stat(smooth_data, X_matrix)
    for cond in range(0,4):
        t_newshape = np.reshape(t[cond,:],vol_shape)
        t_newshape[~in_brain_mask]=np.nan
        t_T = np.zeros(vol_shape)
        for z in range(vol_shape[2]):
            t_T[:, :, z] = t_newshape[:,:, z].T
        t_plot = present_3d(t_T)
        plt.imshow(t_plot,interpolation='nearest', cmap='seismic')
        zero_out=max(abs(np.nanmin(t_T)),np.nanmax(t_T))
        plt.title(name+'_t_statistics'+'_cond_'+'_%s'%(cond+1))
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

#plt.suptitle("Subject 1 Run 1 T Statistics in Condition 4 for different Slices\n")
#plt.colorbar()
#plt.savefig(location_of_plot+"t_statistics_for_condition_4")
#plt.close()


