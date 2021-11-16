#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, '..', 'version.py')) as f:
    exec(f.read())

def find_api(name):
    return f"{name} @ file://localhost/{here}/../{name}#egg={name}"

api = find_api('microns-morphology-api')

base_requires = ['numpy', 'pandas', 'scipy', 'ipyvolume', 'matplotlib', 'tqdm', 'decorator', 'caveclient', 'nglui', api, 'microns-utils@git+https://github.com/cajal/microns-utils.git']
base_api_shared_requires = ['trimesh']

setup(
    name='microns-morphology',
    version=__version__,
    description='Datajoint schemas and methods for morphological analysis/processing of microns data',
    author='Brendan Celii',
    author_email='bac8@rice.edu',
    packages=find_packages(exclude=[]),
    install_requires=[base_requires + base_api_shared_requires]
    
)
