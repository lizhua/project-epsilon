# - compatibility with Python 3
from __future__ import print_function  # print('me') instead of print 'me'
from __future__ import division  # 1/2 == 0.5, not 0
from __future__ import absolute_import
import sys
sys.path.append(".././utils")
# - import common modules
import numpy as np
import matplotlib.pyplot as plt

from find_activated_voxel_functions import *
from convolution_normal_script import X_matrix
import nibabel as nib
from scipy.ndimage import gaussian_filter
from matplotlib import colors
import matplotlib

# import events2neural from stimuli module
from stimuli import events2neural
import nibabel as nib

#import load data modules
from load_BOLD import *

location_of_data="../../data/ds005/"
location_of_plot = "../../plots/"

# Load the sub001 run001 image
data = load_img(1,1)
data = gaussian_filter(data, [2, 2, 2, 0])
# Get the number of volumes
n_trs = data.shape[-1]

#nice map
nice_cmap_values = np.loadtxt('actc.txt')
nice_cmap = colors.ListedColormap(nice_cmap_values, 'actc')

# Identify the TR (time between scans)
TR = 2

# Call the events2neural function to generate the on-off values for each volume
task_name = location_of_data +"sub001/model/model001/onsets/task001_run001/cond002.txt"
task = np.loadtxt(task_name)
time_course = events2neural(task, TR, n_trs)

# Make a single brain volume-size array of all zero to hold the correlations
correlations = np.zeros(data.shape[:-1])

# Loop over all voxel indices on the first, then second, then third dimension
# Extract the voxel time courses at each voxel coordinate in the image
# Get the correlation between the voxel time course and neural prediction
# Fill in the value in the correlations array

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(data.shape[2]):
            vox_values = data[i, j, k]
            correlations[i, j, k] = np.corrcoef(time_course, vox_values)[1, 0]

#set up the label font size
matplotlib.rc('xtick', labelsize=5)
matplotlib.rc('ytick', labelsize=5)

# Plot the correlations array
for i in range(34):
 plt.subplot(5,7,i+1)
 plt.imshow(correlations[:,:,i],cmap = nice_cmap, alpha=0.5)
 plt.title("Slice"+str(i+1), fontsize=5)
 plt.tight_layout()

plt.suptitle("Subject 1 Run 1 Correlation in Condition 2 for Different Slices\n")
plt.colorbar()
plt.savefig(location_of_plot+"correlation_s1r1c2")
