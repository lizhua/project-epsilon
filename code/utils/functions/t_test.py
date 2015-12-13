"""
"""

import sys, os, pdb
import numpy as np
import numpy.linalg as npl
from scipy.stats import t as t_dist
sys.path.append(os.path.join(os.path.dirname(__file__), "./"))
from glm import *

def t_stat(data, X_matrix):
    """
    Return the estimated betas, t-values, degrees of freedom, and p-values for the glm_multi regression
    
    Parameters
    ----------
    data_4d: numpy array of 4 dimensions 
             The image data of one subject, one run
    X_matrix: numpy array 
       The design matrix for glm_multi
    Note that the fourth dimension of `data_4d` (time or the number 
    of volumes) must be the same as the number of rows that X has. 
    
    Returns
    -------
    beta: estimated beta values
    
    t: t-values of the betas
    
    df: degrees of freedom
    
    p: p-values corresponding to the t-values and degrees of freedom
    """

    beta = glm_beta(data, X_matrix)

    # Calculate the parameters - b hat
    beta = np.reshape(beta, (-1, beta.shape[-1])).T

    fitted = X_matrix.dot(beta)
    # Residual error
    y = np.reshape(data, (-1, data.shape[-1]))
    errors = y.T - fitted
    # Residual sum of squares
    RSS = (errors**2).sum(axis=0)
 
    df = X_matrix.shape[0] - npl.matrix_rank(X_matrix)
    # Mean residual sum of squares
    MRSS = RSS / df
    # calculate bottom half of t statistic
    Cov_beta=npl.pinv(X_matrix.T.dot(X_matrix))

    SE =np.zeros(beta.shape)
    for i in range(X_matrix.shape[-1]):
        c = np.zeros(X_matrix.shape[-1])
        c[i]=1
        c = np.atleast_2d(c).T
        SE[i,:]= np.sqrt(MRSS* c.T.dot(npl.pinv(X_matrix.T.dot(X_matrix)).dot(c)))


    zeros = np.where(SE==0)
    SE[zeros] = 1
    t = beta / SE

    t[:,zeros] =0
    # Get p value for t value using CDF of t didstribution
    ltp = t_dist.cdf(abs(t), df)
    p = 1 - ltp # upper tail
    
    return beta.T, t, df, p
