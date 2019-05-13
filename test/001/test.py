# BEGIN: Copyright 
# Copyright (C) 2019 Rector and Visitors of the University of Virginia 
# All rights reserved 
# END: Copyright 

# BEGIN: License 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
#  
#   http://www.apache.org/licenses/LICENSE-2.0 
# END: License 

from nssacPreCommitHook.header import Header
from nssacPreCommitHook.configuration import Configuration
from nssacPreCommitHook.git import Git

configuration = Configuration().loadJsonFile("test/example.json")

git = Git(repo_path="/home/shoops/git/COPASI")

header = Header(git, configuration["copyright"], configuration["license"] if "license" in configuration else None)

# header.updateHeader("/home/shoops/git/COPASI/copasi/model/CModel.cpp", commentStart="//", mode="actual")
header.updateHeader("/home/shoops/git/COPASI/copasi/xml/CopasiML.rng", commentStart="<!--", commentEnd="-->", prolog=[{"end": ">"}], mode="actual")


