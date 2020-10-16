#! /usr/bin/env python
# -*- coding: utf-8 -*-


'''
Copyright (C) 2015 
License: http://www.apache.org/licenses/LICENSE-2.0                 
'''  

from pymap import pyMAP
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
np.set_printoptions(formatter={'float': '{: 13.1f}'.format},linewidth=100)

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

mooring_1 = pyMAP( )

mooring_1.map_set_sea_depth(320)
mooring_1.map_set_gravity(9.81)
mooring_1.map_set_sea_density(1025.0)

mooring_1.read_list_input(nrel5mw_oc4)
#mooring_1.read_file("../test/NRELOffshrBsLine5MW_OC4.map")                            # 200 m depth
#mooring_1.summary_file('name_me.txt')
mooring_1.init( )

epsilon = 1e-5
K = mooring_1.linear(epsilon)    
print("\nHere is the linearized stiffness matrix with zero vessel displacement:")
print(np.array(K))

H,V = mooring_1.get_fairlead_force_2d(0)    
print("Line %d: H = %2.2f [N]  V = %2.2f [N]"%(0, H, V))

fx,fy,fz = mooring_1.get_fairlead_force_3d(0)    
print("Line %d: Fx = %2.2f [N]  Fy = %2.2f [N]  Fz = %2.2f [N]"%(0, fx, fy, fz))

H,V = mooring_1.get_anchor_force_2d(0)    
print("Line %d: H = %2.2f [N]  V = %2.2f [N]"%(0, H, V))

fx,fy,fz = mooring_1.get_anchor_force_3d(0)    
print("Line %d: Fx = %2.2f [N]  Fy = %2.2f [N]  Fz = %2.2f [N]"%(0, fx, fy, fz))

#mooring_1.displace_vessel(5,0,0,0,0,0)
#mooring_1.update_states(0.0,0)

#mooring_1.displace_vessel(17,0,0,0,0,0)
#mooring_1.update_states(0.0,0)

# H,V = mooring_1.get_fairlead_force_2d(0)    
# print(H, "  ", V)

# fx,fy,fz = mooring_1.get_fairlead_force_3d(0)    
# print(fx, "  ", fy, "  ", fz)
# 
# ''' 
# function residual at (hopefully) the solution
# '''
# 
# print(mooring_1.funch(0))
# print(mooring_1.funcl(0))
# 
# '''
# derivatives at solution
# '''
# print(mooring_1.dxdh(0))
# print(mooring_1.dxdv(0))   
# print(mooring_1.dzdh(0))
# print(mooring_1.dzdv(0))
# 
# print(mooring_1.dxdh(1))
# print(mooring_1.dxdv(1))   
# print(mooring_1.dzdh(1))
# print(mooring_1.dzdv(1))

fig = plt.figure()
ax = Axes3D(fig)
for i in range(0,mooring_1.size_lines()):
    x = mooring_1.plot_x( i, 20 )
    y = mooring_1.plot_y( i, 20 )
    z = mooring_1.plot_z( i, 20 )        
    ax.plot(x,y,z,'b-')

ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')        
#ax.set_xlim([-3.0,3])        
#ax.set_ylim([-3.0,3])        
#ax.set_zlim([-3.0,0])        

plt.show()

mooring_1.end( )
