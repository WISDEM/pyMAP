Definitions
===========

What MAP++ Solves
-----------------

Mooring models can be classified into two groups: static models and dynamic models. 
Static models ignore the inertia forces and fluid drag loads, and only account for the mean forces in the mooring system, including elasticity, weight (in fluid), and geometric nonlinearities. 
Static models are the type concerned in MAP++. 
Extra steps are taken to reformulate the classic single line, closed--form solution :cite:`irvine1992` into a piece-wise, multi-sgemented system.
This piece wise system is composed of a collection of nodes and elements.

.. image:: nstatic/bridle2.png
    :width: 48%
.. image:: nstatic/bridle3.png
    :width: 48%

Each element in the figure above is expressed as a single line counterpart in the image below in two configurations. 
One configuration has the line hanging freely, whereas the second orientation account for friction and contact at the bottom boundary. 

Nomenclature
------------

=============  ===============================================================  ============
**Variable**   **Definition**                                                   **Units**
:math:`A`      Cable cross-sectional area                                       [m^2]
:math:`C_B`    Seabed contact friction coefficient                              --
:math:`E`      Young's modulus                                                  [N/m^2]
:math:`g`      Acceleration due to gravity                                      [m/s^2]
:math:`h`      Vertical fairlead excursion                                      [m]
:math:`H`      Horizontal fairlead force                                        [N]
:math:`H_a`    Horizontal anchor force                                          [N]            
:math:`l`      Horizontal fairlead excursion                                    [m]
:math:`L`      Unstretched line length                                          [m]
:math:`L_B`    Line length resting on the seabed                                [m]
:math:`M_j`    Point mass applied to the jth node                               [kg]
:math:`r_i`    Node position vector [xi ; yi ; zi]                              [m]
:math:`s`      Unstretched distance from the anchor (:math:`0 \leq s \leq  L`)  [m]
:math:`T_i`    Cable tension vector                                             [N]
:math:`Te(s)`  Cable tangential tension at distance s                           [N]
:math:`V`      Vertical fairlead force                                          [N]
:math:`V_a`    Vertical anchor force                                            [N]
:math:`x_0`    Horizontal force transition point for :math:`H(s)>0`             [N]                
:math:`R_i`    Rotation angle between the :math:`x_i` and :math:`X` axis        --
:math:`\rho`   Fluid density                                                    [kg/m^3]
=============  ===============================================================  ============
