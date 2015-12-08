
"""
Purpose:
-----------------------------------------------------------------------------------
We generate convolved hemodynamic neural prediction into seperated txt files for 
all four conditions (task, gain, lost, distance), and also generate plots for 4 
BOLD signals over time for each of them too. We use events2neural_high() in stimuli
because the onsets of condition do not start at TR.

Steps:
-----------------------------------------------------------------------------------
1. Extract 4 conditions of subject __'s all run
2. Gain higher time resolutions
3. Convolve with hrf
4. Plot sampled HRFs with the high resolution neural time course
5. Save to txt files
"""

import sys, os
sys.path.append("../utils")
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from stimuli import *
from scipy.stats import gamma
from organize_behavior_data import *
from load_BOLD import *

# Create the necessary directories if they do not exist
dirs = ['../../txt_output', '../../txt_output/conv_high_res',\
        '../../fig','../../fig/conv_high_res']
for d in dirs:
    if not os.path.exists(d):
            os.makedirs(d)

# Locate the different paths
#TODO: the current location for this file project-epsilon/code/scripts
project_path = '../../'
# TODO: change it to relevant path
data_path = project_path+'data/ds005/'

#change here to get your subject !
subject_list = ['11', '5', '1']
#change here to get your run number !
run_list = [str(i) for i in range(1,4)]
cond_list = [str(i) for i in range(1,5)]
images_paths = [('ds005_sub' + s.zfill(3) + '_t1r' + r , \
                 data_path + 'sub' + s.zfill(3) + '/BOLD/task001_run' \
                 + r.zfill(3) + '/bold.nii.gz') for r in run_list \
                 for s in subject_list]

condition_paths = [('ds005_sub' + s.zfill(3) + '_t1r' + r +'_conv_'+ c.zfill(3), \
	data_path + 'sub' + s.zfill(3) + '/model/model001/onsets/task001_run' \
	+ r.zfill(3) + '/cond'+ c.zfill(3) + '.txt') for c in cond_list \
	for r in run_list \
	for s in subject_list]

condition = ['task','gain','loss','dist']
hrf_times = np.arange(0,24,1.0/100)
hrf_at_hr = hrf(hrf_times)

for cond_path in condition_paths:
	name = cond_path[0]
	path = cond_path[1]
	cond = np.loadtxt(path, skiprows = 1)
	# Gain higher time resolutions
	high_res_times, high_cond = events2neural_high(cond)
	# Convolve with hrf
	high_res_hemo = np.convolve(high_cond, hrf_at_hr)[:len(high_cond)]
	tr_indices = np.arange(240)
	tr_times = tr_indices * 2
	# Plot sampled HRFs with the high resolution neural time course
	hr_tr_indices = np.round(tr_indices * 100).astype(int)
	tr_hemo = high_res_hemo[hr_tr_indices]
	plt.plot(tr_times, tr_hemo)
	plt.title(name+'_%s'%(condition[int(path[67])-1]))
	plt.xlabel('Time (seconds)')
	plt.ylabel('Convolved values at TR onsets (condition: %s)'%(condition[int(path[67])-1]))
	plt.savefig(dirs[3]+'/'+ name +'_high_res_.png')
	plt.clf()
	#save the txt file
	np.savetxt(dirs[1] +'/'+ name +'_high_res.txt', tr_hemo)


# # Extract 4 conditions of subject 1's first run
# task, gain, loss, dist = load_model_one(3,1)

# # load data (subject 1 run 1 for now) (you can change it if you want)
# data = load_img(3,1)


# high_res_hemo_gain = np.convolve(high_gain, hrf_at_hr)[:len(high_gain)]
# high_res_hemo_loss = np.convolve(high_loss, hrf_at_hr)[:len(high_loss)]
# high_res_hemo_dist = np.convolve(high_dist, hrf_at_hr)[:len(high_dist)]


# tr_indices = np.arange(240)
# tr_times = tr_indices * 2


# plt.clf()

# tr_hemo_gain = high_res_hemo_gain[hr_tr_indices]
# plt.plot(tr_times, tr_hemo_gain)
# plt.xlabel('Time (seconds)')
# plt.ylabel('Convolved values at TR onsets (condition: gain)')
# plt.savefig(location_of_plot+'gain_high_res_convolution')
# plt.clf()

# tr_hemo_loss = high_res_hemo_loss[hr_tr_indices]
# plt.plot(tr_times, tr_hemo_loss)
# plt.xlabel('Time (seconds)')
# plt.ylabel('Convolved values at TR onsets (condition: loss)')
# plt.savefig(location_of_plot+'loss_high_res_convolution')
# plt.clf()

# tr_hemo_dist = high_res_hemo_dist[hr_tr_indices]
# plt.plot(tr_times, tr_hemo_dist)
# plt.xlabel('Time (seconds)')
# plt.ylabel('Convolved values at TR onsets (condition: dist)')
# plt.savefig(location_of_plot+'dist_high_res_convolution')
# plt.clf()



# create the matrix using np.convolve and plot them
# n_vols = data.shape[-1]
# X_matrix_high_res = np.ones((n_vols,5)) #design matrix (1 at the 0th column)
# condition = [tr_hemo_task, tr_hemo_gain, tr_hemo_loss, tr_hemo_dist]
# for i,name in enumerate(condition):
# 	X_matrix_high_res[:,i+1] = condition[i]




