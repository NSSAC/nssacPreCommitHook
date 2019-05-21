#!/usr/bin/env python3

# BEGIN: Copyright 
# Copyright (C) 2019 Rector and Visitors of the University of Virginia 
# All rights reserved 
# END: Copyright 

# BEGIN: License 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
#   http://www.apache.org/licenses/LICENSE-2.0 
# END: License 

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
          'pathspec',
      ],
      zip_safe=False)
