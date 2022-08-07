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
        K, K2, Kt, Kt2, H, V, fx, fy, fz, Ha, Va, fxa, fya, fza = main(test=True)
        K  = np.asarray(K)
        K2 = np.asarray(K2)


        # Test stiffness matrix
        np.testing.assert_almost_equal(K[0,0], 70734.871793, 2)
        np.testing.assert_almost_equal(K[0,4], -1.09788369931e+5, 2)
        np.testing.assert_almost_equal(K[5,5], 1.172548842785e+8, 2)

        # Test displaced stiffness matrix
        np.testing.assert_almost_equal(K2[0,0], 8.61312155e+04, 2)
            
        # Test linear matrix
        np.testing.assert_almost_equal(Kt[0,0], 70734.871793, 2)
        np.testing.assert_almost_equal(Kt[0,4], -1.094024393e5, 2)
        np.testing.assert_almost_equal(Kt[5,5], 1.172548842785e+8, 2)

        # Test displaced linear matrix
        np.testing.assert_almost_equal(Kt2[0,0], 86131.2141, 2)
        np.testing.assert_almost_equal(Kt2[0,4], -204810.3908, 2)
        np.testing.assert_almost_equal(Kt2[5,5], 1.172548842785e+8, 2)

        # Test fairlead force
        np.testing.assert_almost_equal((fx,fy,fz), (-398302.73, -698649.35,  598004.69), 2)
        # Test anchor force
        np.testing.assert_almost_equal((fxa,fya,fza), (253601.674, 444834.121,-0.), 3)

    def test_stiffness_loads_FST(self):
        # Adding example directory to system path
        sys.path.append(os.path.join(scriptDir,'../examples'))
        from Ex3_StiffnessMatrixFromFST import main
        K, f0 = main(test=True)
        np.testing.assert_almost_equal(K[0,0], 6.53170987e+05, 2)
        np.testing.assert_almost_equal(K[0,2],-1.20267156e+01, 2)
        np.testing.assert_almost_equal(K[0,4],-1.05245632e+07, 0)
        np.testing.assert_almost_equal(K[3,3]/100,  9763474., 0)
        np.testing.assert_almost_equal(K[3,1]/100, 1.05244046e+05,0 )
        np.testing.assert_almost_equal(K[5,5]/100, 4.96403116e+06, 0)
        np.testing.assert_almost_equal(f0[0]    , 5.96711182e+01  ,4)
        np.testing.assert_almost_equal(f0[2]/100, -1.37137573e+05, 0)
        np.testing.assert_almost_equal(f0[4],    -8.68679585e+02 ,4)



if __name__ == '__main__':
    unittest.main()
