""" Linear Regression on Begavioral data """

import sys
sys.path.append(".././utils")
from linear_regression import *

# Get the data
data = combine_all_data()

# Run the linear_regression function to get the summary
linear_regression(data, 'RT', 'gain', 'loss')

linear_regression(data, 'RT', 'ratio')

linear_regression(data, 'RT', 'diff')
