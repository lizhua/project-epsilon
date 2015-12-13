""" Linear Regression on Begavioral data """

import sys
sys.path.append(".././utils")
from organize_behavior_data import *



""" if you want to load and combine 3 behavior datas from 3 runs """

behav=load_behav_txt(3)

""" if you want to load and combine 3 behavior datas from 3 runs in data frame """

behav_df=load_in_dataframe(3)
