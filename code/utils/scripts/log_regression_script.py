""" Linear Regression on Begavioral data """

import sys
sys.path.append(".././utils")
from logistic_reg import *


a=add_gainlossratio(behav_df)
b=organize_columns(a)
log_regression(b)