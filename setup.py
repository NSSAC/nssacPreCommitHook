#!/usr/bin/env python3

from setuptools import setup

setup(name='nssacPreCommitHook',
      version='0.1',
      description='A pre commit hook used to maintain license and copyright information in source files.',
      url='http://github.com/NSSAC/nssacPreCommitHook',
      author='Stefan Hoops',
      author_email='shoops@virginia.edu',
      license='Apache 2.0',
      packages=['nssacPreCommitHook', 'nssacPreCommitHook.git'],
      scripts=["bin/preCommitHook"],
      install_requires=[
          'jsonschema',
      ],
      zip_safe=False)