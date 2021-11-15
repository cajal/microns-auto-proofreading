#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, '..', 'version.py')) as f:
    exec(f.read())

setup(
    name="microns-morphology-api",
    version=__version__,
    description="api for microns-morphology",
    author="Brendan Celii, Christos Papadopoulos",
    packages=find_packages(),
    install_requires = ['trimesh==3.9']
)