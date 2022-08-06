"""
 - Open a MAP input file
 - Perform linearization for various positions
 - Compute fairlead loads 


Copyright (C) 2015                   
License: http://www.apache.org/licenses/LICENSE-2.0                 
"""

from pymap import pyMAP
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # TODO remove me
import numpy as np
#np.set_printoptions(formatter={'float': '{: 13.1f}'.format},linewidth=100)


def main(test=False):

    nrel5mw_oc4 = ['---------------------- LINE DICTIONARY -----------------------------------------------------',
                   'LineType  Diam     MassDenInAir    EA         CB   CIntDamp  Ca   Cdn    Cdt',
                   '(-)       (m)      (kg/m)         (N)        (-)   (Pa-s)    (-)  (-)    (-)',
                   'steel     0.0766  113.35         7.536e8     1.0    1.0E8    0.6 -1.0    0.05',
                   '---------------------- NODE PROPERTIES -----------------------------------------------------',
                   'Node      Type      X        Y         Z        M        V        FX       FY      FZ',
                   '(-)       (-)      (m)      (m)       (m)      (kg)     (m^3)    (kN)     (kN)    (kN)',
                   '1         Fix     418.8    725.383    -200     0        0        #        #       #',
                   '2         Vessel   20.434   35.393     -14.0   0        0        #        #       #',
                   '---------------------- LINE PROPERTIES -----------------------------------------------------',
                   'Line     LineType  UnstrLen   NodeAnch  NodeFair  Flags',
                   '(-)      (-)       (m)        (-)       (-)       (-)',
                   '1        steel     835.35      1         2        plot ',
                   '---------------------- SOLVER OPTIONS-----------------------------------------',
                   'Option',
                   '(-)',
                   'repeat 240 120',
                   'ref_position 0 0 0']



    #moor = pyMAP('inputs/baseline_2.map', WtrDepth=350, gravity=9.81, WtrDens=1025, dllFileName=dllFileName)
    moor = pyMAP()

    # TODO Use Init interface
    moor.map_set_sea_depth(320)
    moor.map_set_gravity(9.81)
    moor.map_set_sea_density(1025.0)
    moor.read_list_input(nrel5mw_oc4)
    #moor.read_file("../test/NRELOffshrBsLine5MW_OC4.map")
    moor.init( ) # TODO remove me

    # --- Plot initial
    # TODO
    #if not test:
    #    fig, ax = moor.plot(numPoints=20, colors=['k'], ls='--')
    
    # --- Linearization with no displacement
    epsilon = 1e-5 # finite difference epsilon
    K = moor.linear(epsilon)    
     
    # --- Linearization with a given surge displacement
    surge = 5.0 # 5 meter surge displacements
    moor.displace_vessel(surge,0,0,0,0,0)
    #moor.update_states(t=0.0, dt=0) TODO
    moor.update_states(0.0, 0)
    K2 = moor.linear(epsilon)    

    # --- Find equilibrium
    # We need to call update states after linearization to find the equilibrium
    #moor.update_states(t=0.0, dt=0) TODO
    moor.update_states(0.0, 0)
    
    # --- Fairlead forces
    line_number = 0
    H,V = moor.get_fairlead_force_2d(line_number)    
      
    fx,fy,fz = moor.get_fairlead_force_3d(line_number)    

    # --- Anchor forces
    Ha,Va = moor.get_anchor_force_2d(0)    

    fxa,fya,fza = moor.get_anchor_force_3d(0)    




    # --- Output 
    if not test:
        print("\nLinearized stiffness matrix with 0.0 vessel displacement:\n")
        print(K)
        print("\nLinearized stiffness matrix with %2.2f surge vessel displacement:\n"%(surge))
        print(K2)
        print("Line %d: H = %2.2f [N]  V = %2.2f [N]"%(line_number, H, V))
        print("Line %d: Fx = %2.2f [N]  Fy = %2.2f [N]  Fz = %2.2f [N]\n"%(line_number, fx, fy, fz))
        print("Line %d: H = %2.2f [N]  V = %2.2f [N]"%(0, Ha, Va))
        print("Line %d: Fx = %2.2f [N]  Fy = %2.2f [N]  Fz = %2.2f [N]"%(0, fxa, fya, fza))
        # TODO
        #print("These values come from the output buffer as defined in the 'LINE PROPERTIES' portion of the input file")
        #print("Labels : ", moor.get_output_labels()[0:6])
        #print("Units  : ", moor.get_output_units()[0:6])
        #v = moor.get_output_buffer()[0:6]
        #print("Values : ", ["{0:0.2f}".format(i) for i in v])

    # --- Plot
    #if not test:
    #    fig, ax = moor.plot(numPoints=20, colors=['b'], fig=fig, ax=ax)
    fig = plt.figure()
    ax = Axes3D(fig)
    for i in range(0,moor.size_lines()):
        x = moor.plot_x( i, 20 )
        y = moor.plot_y( i, 20 )
        z = moor.plot_z( i, 20 )        
        ax.plot(x,y,z,'b-')

    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_zlabel('Z [m]')        
    
    moor.end( )



    return K, K2, H, V, fx, fy, fz, Ha, Va, fxa, fya, fza

if __name__ == '__main__':
    main()
    plt.show()
# if __name__ == '__test__':
#     import platform
#     if platform.system=='Windows':
#         K, H, V, fx, fy, fz = main()
# 
#     np.testing.assert_almost_equal(K[0,0]/1e4,1.98637788, 6)
#     np.testing.assert_almost_equal(K[5,5]/1e8,1.41222256, 6)
#     np.testing.assert_almost_equal(fx/1e5, -5.9751333, 6)
#     np.testing.assert_almost_equal(fz/1e6, 1.14343875, 6)


