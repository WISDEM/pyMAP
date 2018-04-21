#!/usr/bin/env python
# encoding: utf-8

import setuptools
from numpy.distutils.core import setup, Extension
import os
import platform

path = 'src'
bstring_src = ['bstraux.c', 'bstrlib.c']
cminpack_src = ['dpmpar.c', 'enorm.c', 'enorm_u.c',
                'lmder.c', 'lmpar.c', 'qrfac.c',
                'qrsolv.c']
simclist_src = ['simclist.c']
src = ['freedata.c', 'jacobian.c', 'lineroutines.c', 'lmroutines.cc',
       'mapapi.c', 'maperror.c', 'mapinit.c', 'numeric.c', 'outputstream.c',
       'residual.c']
for ifile in xrange(len(bstring_src)):
    bstring_src[ifile] = os.path.join(path, 'map', 'bstring', bstring_src[ifile])
for ifile in xrange(len(cminpack_src)):
    cminpack_src[ifile] = os.path.join(path, 'map', 'cminpack', cminpack_src[ifile])
for ifile in xrange(len(simclist_src)):
    simclist_src[ifile] = os.path.join(path, 'map', 'simclist', simclist_src[ifile])
for ifile in xrange(len(src)):
    src[ifile] = os.path.join(path, 'map', src[ifile])
#src.extend( os.path.join(path, 'pymap', 'mapapi.py') )
src.extend(bstring_src)
src.extend(cminpack_src)
src.extend(simclist_src)

include_dirs = ['bstring','cminpack','lapack','simclist']
for idir in xrange(len(include_dirs)):
    include_dirs[idir] = os.path.join(path, 'map', include_dirs[idir])


if platform.system() == 'Windows':
    cflags = ['-g', '-O1', '-m64', '-std=c99', '-DMAP_DLL_EXPORTS',
              '-DCMINPACK_NO_DLL',  '-DNDEBUG', '-D_WINDOWS', '-D_USRDLL', '-D_MINGW']
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
    py_modules=['pymap'],
    package_data={'pymap': []},
    packages=['pymap'],
    # OS X, Linux
    ext_modules=[Extension('_libmap', sources=src, extra_compile_args=cflags,
                           include_dirs=include_dirs)])


