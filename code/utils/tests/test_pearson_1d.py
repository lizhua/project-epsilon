"""
Test Pearson module, pearson_1d function

Run with::

    nosetests test_pearson_1d.py

This is a test module.
"""
# Python 3 compatibility
from __future__ import absolute_import, division, print_function
from numpy.testing import assert_almost_equal

import numpy as np
import sys, os, pdb

#Specicy the path for functions
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))
import pearson

def test_pearson_1d():
    # Test pearson_1d routine
    x = np.random.rand(22)
    y = np.random.rand(22)
    # Does routine give same answer as np.corrcoef?
    expected = np.corrcoef(x, y)[0, 1]
    actual = pearson.pearson_1d(x, y)
    # Did you, gentle user, forget to return the value?
    if actual is None:
        raise RuntimeError("function returned None")
    assert_almost_equal(expected, actual)
