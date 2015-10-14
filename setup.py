#!/usr/bin/env python

try:
    # If possible, use setuptools
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='pyenvelope',
    version='0.1',
    description='Minimum bounding rectangle calculation',
    author='Andrey Kaygorodov',
    author_email='andreykaygorodov@gmail.com',
    url='https://github.com/kaygorodov/pyenvelope',
    py_modules=['pyenvelope'],
    test_suite='tests',
    install_requires=['Shapely>=1.5.13'],
)
