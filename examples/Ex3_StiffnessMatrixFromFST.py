"""
 - Open an OpenFAST Input File
 - Set up WtrDens, WtrDepth, gravity and MAP input file directly from this input file
 - Compute stiffness matrix and operating point force at a given point
"""

from pymap import pyMAP
import numpy as np
import os

scriptDir = os.path.dirname(__file__)

def main(test=False):

    # --- Setup MAP model from OpenFAST input file
    fstFilename = os.path.join(scriptDir, 'spar/Main.fst')
    moor = pyMAP(fstFilename)

    # --- Stiffness matrix
    K, f0 = moor.stiffness_matrix(epsilon=1e-5, point=(0,0,25))
    
    moor.end()

    return K, f0

if __name__ == '__main__':
    K, f0 = main()
