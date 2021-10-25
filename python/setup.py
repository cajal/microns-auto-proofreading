#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='auto_proofreading',
    version='0.0.1',
    description='Datajoint schemas and methods for auto-proofreading on connectomics data',
    author='Brendan Celii',
    author_email='bac8@rice.edu',
    packages=find_packages(exclude=[]),
    install_requires=['datajoint==0.12.9', 'numpy', 'pandas', 'scipy', 'ipyvolume', 'matplotlib', 'tqdm', 'decorator', 'caveclient', 'nglui']
)