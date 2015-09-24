Release Notes
=============

.. Note::
   Example input files are provided to demonstrate capabilities of MAP. 
   These contrived examples should not be interpreted to represent realistic, practical moorings deployed in the field. 

License
-------
MAP++ is licensed under Apache v 2.0 :ref:`license`

Dependencies
------------
Third party dependencies are distributed with the MAP++ archive on BitBucket. Required libraries include the following:

=====================  =================
**Library**            **Version Distributed with MAP++**
LAPACK                 `Version 3.5.0 <http://www.netlib.org/lapack/>`_
C/C++ Minpack          `Version 1.3.3 <http://devernay.free.fr/hacks/cminpack/>`_
SimCList               `Version 1.6 <http://mij.oltrelinux.com/devel/simclist/>`_
Better String Library  `Version 0.1.1 <http://mike.steinert.ca/bstring/doc/>`_
=====================  =================

Difference Between MAP and MAP++?
---------------------------------
MAP++ (beyond version 1.00.00) is a complete re-write of its predecessor, MAP (up to version 0.97.01). 
MAP++ solves the same problem, integrates into related frameworks, and uses comparable input files to MAP. 
The primary difference is what's under the hood. 
MAP relied on a single, integrated solver to find the solution, and MAP++ uses nested solvers. 
The later architecture improves portability and robustness, but comes at a cost of needing a bit more computational effort. 
MAP++ is written in C, whereas MAP (ironically) was written in C++.  
The '++' suffix indicates an incremental package design from the original inception. 


Change Log
----------

