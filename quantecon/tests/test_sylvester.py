"""
filename: test_sylvester.py
author: Thomas Hasenzagl
email: thomas.hasenzagl@gmail.com
"""

import numpy as np
from numpy.testing import assert_allclose
from scipy import linalg
from quantecon import matrix_eqn as qme


def test_sylvester():
    A = np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    B = np.array([[16, 4, 1], [9, 3, 1], [4, 2, 1]])
    C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    check_sylvester(A, B, C)


def test_cont_lyapunov():
    B = np.array([[16, 4, 1], [9, 3, 1], [4, 2, 1]])
    C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    check_cont_lyapunov(B, C)


def check_sylvester(A, B, C):
    """
    Tests if the solution from solve_sylvester is equal
    to the solution from scipy.linalg.solve_sylvester
    """
    A1 = A 
    B2 = B
    A2 = np.eye(A1.shape[0])
    B1 = np.eye(B2.shape[0])
    M1 = [A1, A2]
    M2 = [B1, B2]
    
    desired = linalg.solve_sylvester(A1, B2, C)
    computed =  qme.solve_sylvester(M1, M2 , C)

    assert_allclose(computed, desired)
    

def check_cont_lyapunov(A, C):   
    """
    Tests if the solution from solve_sylvester is equal
    to the solution from scipy.linalg.solve_lyapunov
    """
    A1 = A
    B2 = A.T
    A2 = np.eye(A1.shape[0])
    B1 = np.eye(B2.shape[0])
    M1 = [A1, A2]
    M2 = [B1, B2]
    
    desired = linalg.solve_lyapunov(A1, C)
    computed =  qme.solve_sylvester(M1, M2, C)

    assert_allclose(computed, desired)
    

