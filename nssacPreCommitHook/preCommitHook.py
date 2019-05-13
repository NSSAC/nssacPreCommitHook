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

import os
import tempfile
from shutil import copyfile
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern

from nssacPreCommitHook.header import Header
from nssacPreCommitHook.configuration import Configuration
from nssacPreCommitHook.git import Status

class PreCommitHook:
    def __init__(self, configFile, git):
        self.configFile = configFile
        self.configuration = Configuration().loadJsonFile(configFile)
        
        if not "license" in self.configuration:
            self.configuration["license"] = None
            
        # Compile the patterns for future use
        for p in self.configuration["patterns"]:
            if "commentEnd" not in p:
                p["commentEnd"] = ""
                
            if "prolog" not in p:
                p["prolog"] = []
                
            p["include"] = PathSpec(map(GitWildMatchPattern, p["include"]))
            
            if "exclude" in p:
                p["exclude"] = PathSpec(map(GitWildMatchPattern, p["exclude"]))
                
        self.git = git
        
        # Change to the git repository directory
        Out, Err, Code = self.git("rev-parse", "--show-toplevel")
        Result = Out.splitlines()
        os.chdir(Result[0])
        
        self.header = Header(self.git, self.configuration["copyright"], self.configuration["license"])
        
        return
    
    def run(self):
        StatusOut, Err, Code = self.git("status", "--porcelain")
        
        for Line in StatusOut.splitlines():
            FileStatus = Status(Line)

            # We only work on staged files which are not deleted
            if not FileStatus.is_staged or FileStatus.is_deleted:
                continue
            
            Pattern = self.findPattern(FileStatus.path)
            
            if not Pattern:
                continue
            
            if FileStatus.is_modified:
                TmpFile = tempfile.mktemp()
                copyfile(FileStatus.path, TmpFile)
                Patch, Err, Code = self.git("diff", "--patch", "--binary", FileStatus.path)
                Checkout, Err, Code = self.git("checkout", "-f", FileStatus.path)
                            
            self.header.updateHeader(FileStatus.path, Pattern["commentStart"], Pattern["commentEnd"], Pattern["prolog"])
            self.git("add", FileStatus.path)
            
            if FileStatus.is_modified:
                Apply, Err, Code = self.git.applyPatch(Patch)
                
                if Code:
                    OutFile = open(FileStatus.path, "w")
                    InFile = open(TmpFile, "r")
                    OutFile.write(InFile.read())
                    OutFile.close()
                    InFile.close()
                    
                os.remove(TmpFile)
                    
    def initRepo(self):
        GitFiles, Err, Code = self.git("ls-files")
        
        for Line in GitFiles.splitlines():
            Pattern = self.findPattern(Line)
            
            if not Pattern:
                continue
            
            self.header.updateHeader(Line, Pattern["commentStart"], Pattern["commentEnd"], Pattern["prolog"])
            self.git("add", Line)
                    
    def findPattern(self, file):
        for p in self.configuration["patterns"]:
            if p["include"].match_file(file) and (not "exclude" in p or not  p["exclude"].match_file(file)):
                return p
        
        return None 
