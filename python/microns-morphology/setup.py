#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, '..', 'version.py')) as f:
    exec(f.read())

def find_config_package(name):
    return f"{name} @ file://localhost/{here}/../{name}#egg={name}"

#config_package = find_config_package('microns-morphology-config')
config_package = find_config_package('microns-morphology-config')

setup(
    name='microns-morphology',
    version=__version__,
    description='Datajoint schemas and methods for morphological analysis/processing of microns data',
    author='Brendan Celii',
    author_email='bac8@rice.edu',
    packages=find_packages(exclude=[]),
    install_requires=[
        #'datajoint==0.12.9',
        'numpy', 'pandas', 'scipy', 'ipyvolume', 'matplotlib', 'tqdm', 'decorator', 'caveclient', 'nglui',config_package
    ]
    
)