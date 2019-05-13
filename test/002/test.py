from nssacPreCommitHook.git import Git
from nssacPreCommitHook.preCommitHook import PreCommitHook

git = Git(repo_path="/home/shoops/git/COPASI")

preCommitHook = PreCommitHook("test/example.json", git)
preCommitHook.run()


