"""
Test Pearson module, pearson_2d function

Run with::

    nosetests test_pearson_2d.py
This is a test module.
"""
# Python 3 compatibility
from __future__ import print_function, division
from numpy.testing import assert_almost_equal

import numpy as np
import sys, os, pdb

#Specify the path for functions
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))
import pearson

def test_pearson_2d():
    # Test pearson_2d routine
    x = np.random.rand(22)
    Y = np.random.normal(size=(22, 12))
    # Does routine give same answers as np.corrcoef?
    expected = np.corrcoef(x, Y.T)[0, 1:]
    actual = pearson.pearson_2d(x, Y)
    # Did you, gentle user, forget to return the value?
    if actual is None:
        raise RuntimeError("function returned None")
    assert_almost_equal(expected, actual)
