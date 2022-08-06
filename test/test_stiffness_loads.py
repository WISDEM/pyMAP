import unittest
import numpy as np    
import sys
import os

scriptDir = os.path.dirname(__file__)

class Test(unittest.TestCase):
    def test_stiffness_loads(self):
        # Adding example directory to system path
        sys.path.append(os.path.join(scriptDir,'../examples'))
        from Ex1_StiffnessMatrixAndLoads import main
        K, K2, H, V, fx, fy, fz, Ha, Va, fxa, fya, fza = main(test=True)
        K  = np.asarray(K)
        K2 = np.asarray(K2)
            
        # Test stiffness matrix
        np.testing.assert_almost_equal(K[0,0], 70734.871793, 2)
        np.testing.assert_almost_equal(K[0,4], -1.094024393e5, 2)
        np.testing.assert_almost_equal(K[5,5], 1.172548842785e+8, 2)

        # Test displaced stiffness matrix
        np.testing.assert_almost_equal(K2[0,0], 86131.2141, 2)
        np.testing.assert_almost_equal(K2[0,4], -204810.3908, 2)
        np.testing.assert_almost_equal(K2[5,5], 1.172548842785e+8, 2)

        # Test fairlead force
        np.testing.assert_almost_equal((fx,fy,fz), (-398302.73, -698649.35,  598004.69), 2)
        # Test anchor force
        np.testing.assert_almost_equal((fxa,fya,fza), (253601.674, 444834.121,-0.), 3)

if __name__ == '__main__':
    unittest.main()
