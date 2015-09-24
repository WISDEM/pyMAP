.. figure:: nstatic/map_logo.png
    :align: center

MAP++ Documentation
===================


.. toctree::
   :maxdepth: 2
   :hidden:

   notes.rst
   definitions.rst
   theory.rst
   input_file.rst
   license.rst
   ref.rst


The Mooring Analysis Program is a software library to model underwater cables held in static equilibrium. 
Because it is a library, MAP is designed to hook into other simulation codes as a tool for prototyping designs, designating a force-diplacements relationship for an arrangement, or include into other dynamic simulation codes to obtain the nonlinear restoring force.
MAP++ is functional on on Windows, Linux, and OSx, with examples for interfacing into Python, C, C++, and Fortran. 
MAP++ follows the FAST Offshore Wind Turbine Framework :cite:`jonkman2013new` software pattern.

More information on the theory behind MAP++ is described :cite:`masciola2013`, with the hopes to extend capabilities to include a heuristic finite element formulation as described :cite:`masciola2014`. MAP++ is licensed under Apache version 2.

.. figure:: nstatic/comparison.png
    :align: center


