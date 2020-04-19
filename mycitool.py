import sys, os, argparse, colorama, docker

from colorama import Fore, Style
from classes.CloneRepo import CloneRepo
from classes.BuildImage import BuildImage

def get_repo_name_from_url(url: str) -> str:
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception(Fore.RED + "Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]
    
def main():
    my_parser = argparse.ArgumentParser(prog='mycitool',
                                    description='Basic CI tool')
    my_parser.add_argument('-b',
                           '--branch',
                           help='clone from a specific branch')

    requiredNamed = my_parser.add_argument_group('required arguments')
    requiredNamed.add_argument('-r', '--repo', help='git URL repository', required=True)
    args = my_parser.parse_args()

    # Initialize variables
    repo_url = ''
    branch = ''

    for arg in vars(args):
        if arg == 'repo':
            repo_url = getattr(args, arg)
        elif arg == 'branch':
            branch = getattr(args, arg)

    repo_name = get_repo_name_from_url(repo_url)
    dir = os.getcwd() + '/' + repo_name

    # Clone the repo
    step1 = CloneRepo(branch)
    step1.clone_repository(repo_url, repo_name)

    # Build Docker image
    client = docker.from_env() 
    step2 = BuildImage(client)
    step2.build_image(dir)


if __name__ == '__main__':
    main()