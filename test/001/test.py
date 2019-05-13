from nssacPreCommitHook.header import Header
from nssacPreCommitHook.configuration import Configuration
from nssacPreCommitHook.git import Git

configuration = Configuration().loadJsonFile("test/example.json")

git = Git(repo_path="/home/shoops/git/COPASI")

header = Header(git, configuration["copyright"], configuration["license"] if "license" in configuration else None)

# header.updateHeader("/home/shoops/git/COPASI/copasi/model/CModel.cpp", commentStart="//", mode="actual")
header.updateHeader("/home/shoops/git/COPASI/copasi/xml/CopasiML.rng", commentStart="<!--", commentEnd="-->", prolog=[{"end": ">"}], mode="actual")


