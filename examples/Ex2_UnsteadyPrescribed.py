"""
 - Open a MAP input file
 - Prescribe a motion of the vessel as function of time
 - Compute fairlead loads 


Adapted from;
    https://bitbucket.org/mmasciola/map-plus-plus/
    Copyright (C) 2015 
    map[dot]plus[dot]plus[dot]help[at]gmail                     
    License: http://www.apache.org/licenses/LICENSE-2.0                 
"""

from pymap import pyMAP
import os
import numpy as np
import matplotlib.pyplot as plt
import numpy as np 
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

scriptDir = os.path.dirname(__file__)

def main(test=False):
    """
    Step 1) First initialize an instance of a mooring system

    Step 2) Assume that (X, Y, Z, phi, theta, psi) are the translation and rotation displacement of the vessel. 
    These displacements are fed into MAP as an argument to displace the fairlead. With the fairlead(s) 
    rigidly connected to the vessel, the (X, Y, Z, phi, theta, psi) directly manifests into the fairlead
    position in the global frame. 
    
    For the time being, assume a sinusoidal displacement of the vessel

    Step 3) This for-loop emulates the time-stepping procedure. You want to loop through the length of 
    the arrays (X,Y,Z,phi,theta,psi) to retrieve the fairlead force

    Step 4) update the MAP state. The arguments in displace_vessel are the displace displacements and rotations about the reference origin. 
    In this case, the reference origin is (0,0,0). 
    They can be set to a different potision using a run-time argument (this is an advanced feature).

    Step 5) get the fairlead tension. The get_fairlead_force_3d returns the fairlead force in 
    X, Y Z coordinates. This must be called at each time-step, and then stored into an array. We append 
    the empty lists created on lines 84-88.

    .. Note::

       MAP does *NOT* return the mooring restoring moment, The user must calculate this 
       themself using the cross-product between the WEC reference origin and the mooring attached
       point, i.e.,
    
       :math:`\mathbf{Moment} = \mathbf{r} \times \mathbf{F}`
    """

    # --- Initialize mooring model
    mooring = pyMAP(os.path.join(scriptDir,'inputs/baseline_1.map'), WtrDepth=120, gravity=9.81, WtrDens=1020) 

    # --- Plot 
    fig, ax = mooring.plot(numPoints=20) # Optional: call the user function to illustrate the mooring equilibrium profile
    

    # --- Setup motion
    # initialize list to zero (this is artificial. This would be prescribed the by vessel program)
    X,Y,Z,phi,theta,psi = (np.zeros(500) for _ in range(6))
    time = []
    # variable to specify the amplitude of surge oscillation and period factor
    dt = 0.1
    amplitude = 10.0
    # prescribe artificial surge and pitch displacement. Again, this should be supplied based on the WEC motion or from time-marching routine
    for i in range(len(X)):
        time.append(i*dt)
        X[i] = (amplitude)*(np.sin(i*0.05))
        theta[i] = (amplitude)*(np.sin(i*0.025))

    # Storage for line tension
    f_line1 = np.zeros((len(X),3)) # fx, fy, fz
    f_line2 = np.zeros((len(X),3))
    f_line3 = np.zeros((len(X),3))
    f_line4 = np.zeros((len(X),3))

    # --- Step 3) Time marching
    for i in range(len(X)):        
        # Step 4) 

        # displace the vessel, X,Y,X are in units of m, and phi, theta, psi are in units of degrees
        mooring.displace_vessel(X[i], Y[i], Z[i], phi[i], theta[i], psi[i]) 

        # first argument is the current time. Second argument is the coupling interval (used in FAST)
        mooring.update_states(time[i], 0)                                   

        # Step 5) 
        # line 1 tensions in X, Y and Z. Note that python is indexed started at zero
        f_line1[i,:] = mooring.get_fairlead_force_3d(0) # arugment is the line number

        # line 2 tensions in X, Y and Z.
        f_line2[i,:] = mooring.get_fairlead_force_3d(1)

        # line 3 tensions in X, Y and Z.
        f_line3[i,:] = mooring.get_fairlead_force_3d(2)

        # line 4 tensions in X, Y and Z.
        f_line4[i,:] = mooring.get_fairlead_force_3d(3)

    # Optional: plot the vessel displacement (surge=X and pitch=theta) as a function of time
    plt.figure(2)
    plt.plot(time,X,lw=2,label='Surge displacement')
    plt.plot(time,theta,lw=2,label='Pitch displacement')
    plt.title('Vessel Translation/Rotation')
    plt.ylabel('Amplitude [m,deg]')
    plt.xlabel('Time [sec]')
    plt.legend()

    # Optional: plot line tension time history
    plt.figure(3)
    ax=plt.subplot(3,1,1)
    plt.plot(time,f_line1[:,0],label='Line 1')
    plt.plot(time,f_line2[:,0],label='Line 2')
    plt.plot(time,f_line3[:,0],label='Line 3')
    plt.plot(time,f_line4[:,0],label='Line 4')
    plt.ylabel('X Fairlead Force [N]')
    plt.legend()

    ax = plt.subplot(3,1,2)
    plt.plot(time,f_line1[:,1])
    plt.plot(time,f_line2[:,1])
    plt.plot(time,f_line3[:,1])
    plt.plot(time,f_line4[:,1])
    plt.ylabel('Y Fairlead Force [N]')

    ax = plt.subplot(3,1,3)
    plt.plot(time,f_line1[:,2])
    plt.plot(time,f_line2[:,2])
    plt.plot(time,f_line3[:,2])
    plt.plot(time,f_line4[:,2])
    plt.ylabel('Z Fairlead Force [N]')
    plt.xlabel('Time [s]')

    return f_line1, f_line2, f_line3, f_line4


if __name__ == '__main__':      
    main()
    plt.show()
