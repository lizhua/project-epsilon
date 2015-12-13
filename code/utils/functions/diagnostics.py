""" Diagnostics.py

A collection of utility functions for diagnostics on FMRI data

See test_* functions in this directory for nose tests
"""

import numpy as np


def vol_std(data):
    """ Return standard deviation across voxels for 4D array `data`

    Parameters
    ----------
    data : 4D array
        4D array from FMRI run with last axis indexing volumes.  Call the shape
        of this array (M, N, P, T) where T is the number of volumes.

    Returns
    -------
    std_values : array shape (T,)
        One dimensonal array where ``std_values[i]`` gives the standard
        deviation of all voxels contained in ``data[..., i]``.
    """
    T = data.shape[-1]
    data_2d = np.reshape(data, (-1, T))
    return np.std(data_2d, axis=0)


def iqr_outliers(arr_1d, iqr_scale=1.5):
    """ Return indices of outliers identified by interquartile range

    Parameters
    ----------
    arr_1d : 1D array
        One-dimensional numpy array, from which we will identify outlier
        values.
    iqr_scale : float, optional
        Scaling for IQR to set low and high thresholds.  Low threshold is given
        by 25th centile value minus ``iqr_scale * IQR``, and high threshold id
        given by 75 centile value plus ``iqr_scale * IQR``.

    Returns
    -------
    outlier_indices : array
        Array containing indices in `arr_1d` that contain outlier values.
    lo_hi_thresh : tuple
        Tuple containing 2 values (low threshold, high thresold) as described
        above.
    """
    # Hint : np.lookfor('centile')
    # Hint : np.lookfor('nonzero')
    pct_25, pct_75 = np.percentile(arr_1d, [25, 75])
    iqr = pct_75 - pct_25
    lo_thresh = pct_25 - iqr * iqr_scale
    hi_thresh = pct_75 + iqr * iqr_scale
    is_outlier = (arr_1d < lo_thresh) | (arr_1d > hi_thresh)
    return np.nonzero(is_outlier)[0], (lo_thresh, hi_thresh)


def vol_rms_diff(arr_4d):
    """ Return root mean square of differences between sequential volumes

    Parameters
    ----------
    data : 4D array
        4D array from FMRI run with last axis indexing volumes.  Call the shape
        of this array (M, N, P, T) where T is the number of volumes.

    Returns
    -------
    rms_values : array shape (T-1,)
        One dimensonal array where ``rms_values[i]`` gives the square root of
        the mean (across voxels) of the squared difference between volume i and
        volume i + 1.
    """
    T = arr_4d.shape[-1]
    diff_data = np.diff(arr_4d, axis=-1)
    diff_data_2d = np.reshape(diff_data, (-1, T-1))
    return np.sqrt(np.mean(diff_data_2d ** 2, axis=0))


def extend_diff_outliers(diff_indices):
    """ Extend difference-based outlier indices `diff_indices` by pairing

    Parameters
    ----------
    diff_indices : array
        Array of indices of differences that have been detected as outliers.  A
        difference index of ``i`` refers to the difference between volume ``i``
        and volume ``i + 1``.

    Returns
    -------
    extended_indices : array
        Array where each index ``j`` in `diff_indices has been replaced by two
        indices, ``j`` and ``j+1``, unless ``j+1`` is present in
        ``diff_indices``.  For example, if the input was ``[3, 7, 8, 12, 20]``,
        ``[3, 4, 7, 8, 9, 12, 13, 20, 21]``.
    """
    # Make two columns with the second being the first plus 1
    ext_outliers = np.column_stack((diff_indices, diff_indices + 1))
    # Use numpy reshape ordering to get the values from the first row, then the
    # second row etc...
    return np.unique(ext_outliers.ravel())
