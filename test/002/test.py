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

from nssacPreCommitHook.git import Git
from nssacPreCommitHook.preCommitHook import PreCommitHook

git = Git(repo_path="/home/shoops/git/COPASI")

preCommitHook = PreCommitHook("test/example.json", git)
preCommitHook.run()


