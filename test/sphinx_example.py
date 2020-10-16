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
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

baseline2 = ['--------------- LINE DICTIONARY -------------------------',
             'LineType  Diam      MassDenInAir   EA        CB   CIntDamp  Ca    Cdn    Cdt',
             '(-)       (m)       (kg/m)        (N)        (-)   (Pa-s)   (-)   (-)    (-)',
             'steel     0.25       320.0     9800000000   1.0    -999.9 -999.9 -999.9 -999.9',
             'nylon     0.30       100.0     980000000    1.0    -999.9 -999.9 -999.9 -999.9',
             '--------------- NODE PROPERTIES -------------------------',
             'Node Type       X       Y       Z      M     B     FX    FY    FZ',
             '(-)  (-)       (m)     (m)     (m)    (kg)  (mˆ3)  (N)   (N)   (N)',
             '1    Fix     400        0     depth    0     0      #     #     #',
             '2    Connect #90       #0    #-80      0     0      0     0     0   ',
             '3    Vessel   20        20    -10      0     0      #     #     #',
             '4    Vessel   20       -20    -10      0     0      #     #     #',
             '--------------- LINE PROPERTIES -------------------------',
             'Line    LineType  UnstrLen  NodeAnch  NodeFair  Flags',
             '(-)      (-)       (m)       (-)       (-)       (-)',
             '1       steel      450        1         2    ',
             '2       nylon      90         2         3    ',
             '3       nylon      90         2         4    ',
             '--------------- SOLVER OPTIONS---------------------------',
             'Option',
             '(-)',
             ' help',
             'outer_tol 1e-5',
             'repeat 120 ',
             'repeat 240']

mooring_1 = pyMAP()

mooring_1.map_set_sea_depth(350)      # m
mooring_1.map_set_gravity(9.81)       # m/s^2
mooring_1.map_set_sea_density(1025.0) # kg/m^3

mooring_1.read_list_input(baseline2)
#mooring_1.read_file("baseline_2.map") 
#mooring_1.summary_file('summary_file.txt')

mooring_1.init( )

epsilon = 1e-3 # finite difference epsilon
K = mooring_1.linear(epsilon)    
print("\nLinearized stiffness matrix with 0.0 vessel displacement:\n")
print(np.array(K))

surge = 5.0 # 5 meter surge displacements
mooring_1.displace_vessel(surge,0,0,0,0,0)
mooring_1.update_states(0.0,0)

K = mooring_1.linear(epsilon)    
print("\nLinearized stiffness matrix with %2.2f surge vessel displacement:\n"%(surge))
print(np.array(K))

# We need to call update states after linearization to find the equilibrium
mooring_1.update_states(0.0,0)

line_number = 0
H,V = mooring_1.get_fairlead_force_2d(line_number)    
print("Line %d: H = %2.2f [N]  V = %2.2f [N]"%(line_number, H, V))

fx,fy,fz = mooring_1.get_fairlead_force_3d(line_number)    
print("Line %d: Fx = %2.2f [N]  Fy = %2.2f [N]  Fz = %2.2f [N]"%(line_number, fx, fy, fz))

H,V = mooring_1.get_anchor_force_2d(line_number)    
print("Line %d: H = %2.2f [N]  V = %2.2f [N]"%(line_number, H, V))

fx,fy,fz = mooring_1.get_anchor_force_3d(line_number)    
print("Line %d: Fx = %2.2f [N]  Fy = %2.2f [N]  Fz = %2.2f [N]"%(line_number, fx, fy, fz))


fig = plt.figure()
ax = Axes3D(fig)
num_points = 20
for i in range(0,mooring_1.size_lines()):
    x = mooring_1.plot_x(i, num_points)
    y = mooring_1.plot_y(i, num_points)
    z = mooring_1.plot_z(i, num_points)        
    ax.plot(x,y,z,'b-')

ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')        

plt.show()

mooring_1.end( )
