#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup
from numpy.distutils.core import setup, Extension
import os
import sys
import platform
import glob

os.environ['NPY_DISTUTILS_APPEND_FLAGS'] = '1'

if platform.system() == 'Windows':
    # For Anaconda
    cflags = ['-O1', '-m64', '-fPIC', '-std=c99','-DCMINPACK_NO_DLL']
elif sys.platform == 'cygwin':
    cflags = ['-O1', '-m64', '-fPIC', '-std=c99']
elif platform.system() == 'Darwin':
    cflags = ['-O1', '-m64', '-fno-omit-frame-pointer', '-fPIC']#, '-std=c99']
else:
    #cflags = ['-O1', '-m64', '-fPIC', '-std=c99', '-D WITH_LAPACK']
    cflags = ['-O1', '-m64', '-fPIC', '-std=c99']

pymapExt   = Extension('_libmap', sources=glob.glob(os.path.join('src','pymap','**','*.c'), recursive=True)+
                       glob.glob(os.path.join('src','pymap','**','*.cc'), recursive=True),
                       extra_compile_args=cflags,
                       include_dirs=[os.path.join('src','pymap','lapack')])
    
setup(
    name='pyMAP',
    version='1.0.0',
    description='Python module wrapping around MAP++',
    author='NREL WISDEM Team',
    author_email='systems.engineering@nrel.gov',
    license='Apache License, Version 2.0',
    package_dir={'': 'src'},
    py_modules=['pymap'+os.sep+'pymap'],
    package_data={'pymap': []},
    packages=['pymap'],
    ext_modules=[pymapExt],
    zip_safe=False
)


