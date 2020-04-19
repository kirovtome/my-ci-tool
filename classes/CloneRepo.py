import os, git, colorama, sys

from git import Repo
from colorama import Fore, Style


class CloneRepo:

    def __init__(self, branch):
        self.branch = branch

    def clone_repository(self, repo_url, repo_name):
        dir = os.getcwd() + '/' + repo_name

        #Clone repo
        print ('Cloning repository into ',dir,'...')
        try:
            cloned_repo = Repo.clone_from(repo_url, repo_name, branch=self.branch)
        except git.GitCommandError as e:
            print (Fore.RED + e.stderr)
            sys.exit()