#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup
from numpy.distutils.core import setup, Extension
import os
import sys
import platform

path = 'src' + os.sep + 'pymap'
bstring_src = ['bstraux.c', 'bstrlib.c']
cminpack_src = ['dpmpar.c', 'enorm.c', 'enorm_u.c',
                'lmder.c', 'lmpar.c', 'qrfac.c',
                'qrsolv.c']
simclist_src = ['simclist.c']
src = ['freedata.c', 'jacobian.c', 'lineroutines.c', 'lmroutines.cc',
       'mapapi.c', 'maperror.c', 'mapinit.c', 'numeric.c', 'outputstream.c',
       'residual.c']
for ifile in xrange(len(bstring_src)):
    bstring_src[ifile] = os.path.join(path, 'bstring', bstring_src[ifile])
for ifile in xrange(len(cminpack_src)):
    cminpack_src[ifile] = os.path.join(path, 'cminpack', cminpack_src[ifile])
for ifile in xrange(len(simclist_src)):
    simclist_src[ifile] = os.path.join(path, 'simclist', simclist_src[ifile])
for ifile in xrange(len(src)):
    src[ifile] = os.path.join(path, src[ifile])
src.extend(bstring_src)
src.extend(cminpack_src)
src.extend(simclist_src)

include_dirs = ['bstring','cminpack','lapack','simclist']
for idir in xrange(len(include_dirs)):
    include_dirs[idir] = os.path.join(path, include_dirs[idir])


if platform.system() == 'Windows':
    # Note that there are unresolved problems building the extension with mingw and
    # then linking with Python (built with MSC)
    #cflags = ['-g','-O1','-m64','-std=c99','-DCMINPACK_NO_DLL','-D_WIN32','-D_MSC_VER']
    cflags = ['/g','/O1','/m64','/DCMINPACK_NO_DLL','/D_WIN32','/D_MSC_VER']
elif sys.platform == 'cygwin':
    cflags = ['-g', '-O1', '-m64', '-fPIC', '-std=c99']
elif platform.system() == 'Darwin':
    cflags = ['-g', '-O1', '-m64', '-fno-omit-frame-pointer', '-fPIC']#, '-std=c99']
else:
    cflags = ['-g', '-O1', '-m64', '-fPIC', '-std=c99', '-D WITH_LAPACK']

setup(
    name='pyMAP',
    version='1.0.0',
    description='Python module wrapping around MAP++',
    author='Garrett Barter',
    author_email='garrett.barter@nrel.gov',
    license='Apache License, Version 2.0',
    package_dir={'': 'src'},
    py_modules=['pymap'+os.sep+'pymap'],
    package_data={'pymap': []},
    packages=['pymap'],
    ext_modules=[Extension('_libmap', sources=src, extra_compile_args=cflags,
                           include_dirs=include_dirs)],
    zip_safe=False
)


