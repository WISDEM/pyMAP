import unittest
import numpy as np    
import sys
import os

scriptDir = os.path.dirname(__file__)

class Test(unittest.TestCase):
    def test_stiffness_loads(self):
        # Adding example directory to system path
        sys.path.append(os.path.join(scriptDir,'../examples'))
        from Ex2_UnsteadyPrescribed import main
        f1, f2, f3, f4 = main(test=True)

        # Test final value of line tension
        np.testing.assert_almost_equal(f1[-1,:], [ -3664.46, 746558.92, 612870.14], 2)
        np.testing.assert_almost_equal(f2[-1,:], [691466.56,      0.  , 596978.59], 2)
        np.testing.assert_almost_equal(f3[-1,:], [  -3664.46, -746558.92,  612870.14], 2)
        np.testing.assert_almost_equal(f4[-1,:], [-814702.  ,       0.  ,  632743.62], 2)

if __name__ == '__main__':
    unittest.main()
