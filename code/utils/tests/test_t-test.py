"""test_t-test.py
Tests for the functions in the t-test.py

Run with:
    nosetests test_t-test.py
"""
from __future__ import print_function
import os, sys
import numpy as np
from numpy.testing import assert_almost_equal, assert_array_equal

#Append path to functions
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))
from t_test import t_stat 


def test_t_stat():
    psychopathy = [11.416,   4.514,  12.204,  14.835,
                   8.416,   6.563,  17.343, 13.02,
            		   15.19 ,  11.902,  22.721,  22.324]
    clammy = [0.389,  0.2  ,  0.241,  0.463,
              4.585,  1.097,  1.642,  4.972,                                
	      7.957,  5.585,  5.527,  6.964]
    age = [22.5,  25.3,  24.6,  21.4,
           20.7,  23.3,  23.8,  21.7,
           21.3, 25.2,  24.6,  21.8]
    X = np.column_stack((np.ones(12), clammy))
    Y = np.asarray(psychopathy)
    B, t, df, p = t_stat(Y, X)
    assert_array_equal((np.around(t[1][:6],6),np.around(p[1][:6],6)),
           ( [1.914389], [0.042295]))
