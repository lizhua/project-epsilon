"""
Purpose:
-----------------------------------------------------------------------------------
We make the extraction of txt file to be easier by building these functions. 
-----------------------------------------------------------------------------------
"""



import numpy as np
import pandas as pd

project_location="../../"
data_location=project_location+"data/ds005/"

"""load and combine 3 behavior datas from 3 runs"""
def load_behav_txt(subject_number):
	""" Return the subject behav data combining all 3 runs and excluding invalid data (-1) in np.array

    Parameters
    ----------
    subject_number : int
    	Subject Number
    
    Returns
    -------
    behav_total_run : np.array
    	the subject's behav data (combining all 3 runs)
        
    """

	#load texts
	behav1=np.loadtxt(data_location+'sub00%s/behav/task001_run001/behavdata.txt'%(subject_number),skiprows=1)
	behav2=np.loadtxt(data_location+'sub00%s/behav/task001_run002/behavdata.txt'%(subject_number),skiprows=1)
	behav3=np.loadtxt(data_location+'sub00%s/behav/task001_run003/behavdata.txt'%(subject_number),skiprows=1)
	
	#concatenate them to be 1
	behav_total_run=np.concatenate((behav1,behav2,behav3),axis=0)

	#delete the rows that contain -1 in respcat (these are errors in experiment so we should take them out
	behav_total_run=np.delete(behav_total_run, np.where(behav_total_run[:,5]==-1),axis=0)		
		
	print('your behav_total_run is ready to use!')

	return behav_total_run


def load_behav_text_one(subject_number, run_number):
	""" Return the subject behav data (single run) in np.array

    Parameters
    ----------
    subject_number : int
    	Subject Number
    run_number : int
    	Run Number	
    
    Returns
    -------
    behav_total_run : data.frame
    	the subject's behav data (single run)
        
    """

	behav=np.loadtxt(data_location+'sub00%s/behav/task001_run00%s/behavdata.txt'%(subject_number,run_number),
		skiprows=1)

	#delete the rows that contain -1 in respcat (these are errors in experiment so we should take them out
	behav_run=np.delete(behav, np.where(behav[:,5]==-1),axis=0)		
	print('your behav_run is ready to use!')

	return behav_run



def load_in_dataframe(subject_number):
	""" Return the subject behav data combining all 3 runs and excluding invalid data (-1) in data.frame

    Parameters
    ----------
    subject_number : int
    	Subject Number
    
    Returns
    -------
    behav_total_run : data.frame
    	the subject's behav data (combining all 3 runs)
        
    """

	#convert 3 behavior datas in 1 subject into data frames.
	run1 = pd.read_table(data_location+'sub00%s/behav/task001_run001/behavdata.txt'%(subject_number))
	run2 = pd.read_table(data_location+'sub00%s/behav/task001_run002/behavdata.txt'%(subject_number))
	run3 = pd.read_table(data_location+'sub00%s/behav/task001_run003/behavdata.txt'%(subject_number))

	#append all the runs in one pandas data frame
	r=run1.append(run2)
	run_total=r.append(run3) 
	
	return run_total







	