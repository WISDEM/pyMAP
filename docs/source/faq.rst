FAQ
===

Using with Python
-----------------

''Python doesn't work''
~~~~~~~~~~~~~~~~~~~~~~~

If importing MAP++ into Python leads to this error on Linux/OSx: 
 
.. code-block:: bash

    OSError: ../src/libmap-1.20.00.so: cannot open shared object file: No such file or directory

or on Windows:

.. code-block:: bash

    WindowsError: [Error 126] The specified module could not be found

then the issue is the MAP++ shared object/dll can't be located by the MAP++ module. 
This is corrected by changing the path where the .so/.dll is picked up in ``mapsys.py``:

.. code-block:: python

    lib = cdll.LoadLibrary("/directory/to/map/libmap-1.20.00.so")

On Windows, it would look something like this:

.. code-block:: python

    lib = cdll.LoadLibrary("C:\User\local\directory\map_x64.dll")  


Initialization Errors
---------------------

I get WARNING [5] or FATAL [41] and can't emerge from initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The error thrown at initialization is either:

.. code-block:: bash

    MAP_WARNING[5] : Cable density is approaching the density of seawater. 
                     This may result in the problem becoming poorly conditioned. 

or

.. code-block:: bash

    MAP_FATAL[41] : Cable mass density is zero. Neutrally buoyant cables cannot 
                    be solved using quasi-statis model

We insert a check to warning the user if the cable is nearly neutrally buoyant. 
This causes the solver to go on the fritz, and sometimes fail, because the algebraic equation is close to dividing by zero; see :ref:`the horizontal cable equation <eq_horizontal>`.
The straightforward way to fix this is to change :math:`\omega` tolerance levels in ``mapinit.c`` 
The default tolerance levels are omega :math:`\omega< 1.0` for a warning, and omega :math:`\omega<10^{-3}` for fatal. 
In some cases, this is unavoidable and a different mooring program is needed. 

.. literalinclude:: ../../src/mapinit.c
   :language: c
   :start-after: library_iter->a = area;
   :end-before: end read
   :linenos:
   :emphasize-lines: 1,8

.. todo:: Include a run-time tolerance override option in the input file. 


Maximum iterations are exceeded with taut mooring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The mooring system probably has a connect node. 
I'd start by increasing ``OUTER_TOL`` by an order of magnitude more than the :ref:`default option <default_options>`. 
It doesn't take much displacement error in the inner solve to cause a large difference in the outer loop, so there's this constant game of playing catch-up. 
Alternatively, you can decrease the inner loop solve tolerance, but you might be already approaching machine precision. 
Taut lines are strange like that. 

A good solver option/initial guess strategy should converge on a solution in under 100-500 total iterations in the first solve.
