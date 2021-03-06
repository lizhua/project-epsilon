"""
This script create a bash script to be used in the Makefile of the data directory.
It will download the filtered data from from 
https://nipy.bic.berkeley.edu/rcsds/ds005/
and locate them in the relevant local directories
"""
import os
import pdb
import numpy as np

project_id = 'ds005'
subject_N = 16
run_N = 3

project_path = '../'
data_path = project_path + 'data/'
#subject_list = [str(i) for i in range(1,subject_N+1)]
subject_list = [str(i) for i in range(1,2)]
run_list = [str(i) for i in range(1,run_N+1)]
base_url = 'https://nipy.bic.berkeley.edu/rcsds/%s/'%(project_id)
file_name = 'filtered_func_data_mni.nii.gz'

#Write local downloading location and link on txt file
txt_out = []
mkdir_out = []
for s in subject_list:
    for r in run_list:
        wget = 'wget --no-check-certificate '
        location = data_path + '%s_filtered/sub'%(project_id) + s.zfill(3)\
           +'/BOLD/task001_run%s/'%(r.zfill(3))
        link = base_url + 'sub%s/model/model001/task001_run' %(s.zfill(3))\
               + r.zfill(3) + '.feat/' + file_name
        txt_out.append((wget + link + ' -O ' + location + 'bold_filtered.nii.gz'))
        mkdir_out.append(('mkdir -p ' + location))

np_txt_out = np.array((txt_out))
np_mkdir_out = np.array((mkdir_out))
np_out = np.vstack((np_mkdir_out,np_txt_out)).ravel([-1])
np.savetxt(data_path + 'dwn_filtered_data_script.sh', np_out, delimiter=" ", fmt="%s")
