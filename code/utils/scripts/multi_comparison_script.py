
"""
Purpose:
-----------------------------------------------------------------------------------
We seek the activated voxel positionsi through multi-comparison of beta values across
subjects

Step
-----------------------------------------------------------------------------------
1. calculate the mean of each single beta values across subject and plot them
2. calculate the variance of each single beta values across subject and plot them
3. calculate the t-stat of each single beta values across subject and plot them
4. ????? 
"""


import sys, os
##sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
import numpy as np
from glm import *
#from convolution_normal_script import X_matrix
#from convolution_high_res_script import X_matrix_high_res
from load_BOLD import *
import nibabel as nib
import matplotlib.pyplot as plt
from smoothing import *


dirs = ['../../../txt_output/multi_beta']

task = dict()
gain = dict()
loss = dict()
dist = dict()

#load all of them
for x in range(1,17):
	task[x] = np.load(dirs[0]+'/ds005_sub'+str(x).zfill(3)+'_t1r1_beta_task.npy')

for x in range(1,17):
	gain[x] = np.load(dirs[0]+'/ds005_sub'+str(x).zfill(3)+'_t1r1_beta_gain.npy')

for x in range(1,17):
	loss[x] = np.load(dirs[0]+'/ds005_sub'+str(x).zfill(3)+'_t1r1_beta_loss.npy')

for x in range(1,17):
	dist[x] = np.load(dirs[0]+'/ds005_sub'+str(x).zfill(3)+'_t1r1_beta_dist.npy')

#calculate mean and plot (let's try for task)
task_sum = task[1]
for x in range(2,17):
	task_sum +=task[x]

task_mean = task_sum/16

#calculate variance and plot



#calculate t-test and plot








