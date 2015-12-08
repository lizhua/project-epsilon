
"""
Purpose:
-----------------------------------------------------------------------------------
We generate convolved hemodynamic neural prediction into seperated txt files for 
all four conditions (task, gain, lost, distance), and also generate plots for 4 
BOLD signals over time for each of them too. 

Steps:
-----------------------------------------------------------------------------------
1. Extract 4 conditions of subject __'s first run
2. Load the data to get the 4th dimension shape
3. Convolve with hrf
4. Plot sampled HRFs with the high resolution neural time course
5. Save the convolved data into txt files
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
dirs = ['../../txt_output', '../../txt_output/conv_normal',\
        '../../fig','../../fig/conv_normal']
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
#TODO: change here later
images_paths = [('ds005_sub' + s.zfill(3) + '_t1r' + r , \
                 data_path + 'sub' + s.zfill(3) + '/BOLD/task001_run' \
                 + r.zfill(3) + '/bold.nii') for r in run_list \
                 for s in subject_list]

condition_paths = [('ds005_sub' + s.zfill(3) + '_t1r' + r +'_conv_'+ c.zfill(3), \
	data_path + 'sub' + s.zfill(3) + '/model/model001/onsets/task001_run' \
	+ r.zfill(3) + '/cond'+ c.zfill(3) + '.txt') for c in cond_list \
	for r in run_list \
	for s in subject_list]

condition = ['task','gain','loss','dist']

#get the dimension for data
img = nib.load(images_paths[0][1])
data = img.get_data()
#set the TR
TR = 2.0
#get canonical hrf
tr_times = np.arange(0, data.shape[2], TR)
hrf_at_trs = hrf(tr_times)
n_vols = data.shape[-1]
vol_shape = data.shape[:-1]
all_tr_times = np.arange(data.shape[-1]) * TR

for cond_path in condition_paths:
	name = cond_path[0]
	path = cond_path[1]
	cond = np.loadtxt(path, skiprows = 1)
	neural_prediction = events2neural(cond,TR,n_vols)
	convolved = np.convolve(neural_prediction, hrf_at_trs)
	convolved = convolved[:-(len(hrf_at_trs)-1)]
	#plot
	plt.plot(all_tr_times, neural_prediction)
	plt.plot(all_tr_times, convolved)
	plt.title(name+'_%s'%(condition[int(path[67])-1]))
	plt.xlabel('Time (seconds)')
	plt.ylabel('Convolved values at TR onsets (condition: %s)'%(condition[int(path[67])-1]))
	plt.savefig(dirs[3]+'/'+ name +'_canonical.png')
	plt.clf()
	#save the txt file
	np.savetxt(dirs[1] +'/'+ name +'_canonical.txt', convolved)



# # Extract 4 conditions of subject 1's first run
# task, gain, loss, dist = load_model_one(1,1)

# # load data (subject 1 run 1 for now) ( you can change it if you want )
# data = load_img(1,1)


# TR = 2.0
# tr_times = np.arange(0, data.shape[2], TR)
# hrf_at_trs = hrf(tr_times)
# n_vols = data.shape[-1]
# X_matrix = np.ones((n_vols,5)) #design matrix (1 at the 0th column)


# # create the matrix using np.convolve and plot them
# all_tr_times = np.arange(data.shape[-1]) * TR
# condition = [task, gain, loss, dist]
# condition_string = ['task', 'gain', 'loss', 'dist']
# for i,name in enumerate(condition):
# 	neural_prediction = events2neural(name,TR,n_vols)
# 	convolved = np.convolve(neural_prediction, hrf_at_trs)
# 	convolved = convolved[:-(len(hrf_at_trs)-1)]
# 	plt.plot(all_tr_times, neural_prediction)
# 	plt.plot(all_tr_times, convolved)
# 	plt.xlabel("time")
# 	plt.ylabel("HRF")
# 	plt.title("Condition %s"%(condition_string[i]))
# 	plt.savefig(location_of_plot+"convolved_%s.png"%(condition_string[i]))
# 	plt.clf()
# 	np.savetxt(location_of_txt+'ds005_sub001_t1r1_conv%s.txt'%(i+1), convolved)
# 	X_matrix[:,i+1] = convolved

# # Your X_matrix is ready



