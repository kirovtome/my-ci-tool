import sys, docker, colorama

from colorama import Fore, Style
from docker.errors import APIError

class BuildImage:

    def __init__(self, client):
        self.client = client 
        
    def build_image(self, dir):
        print ('Building image and starting container(s) ...')
        try:
            self.client.images.build(path=dir)
            print (Fore.GREEN + 'OK')
        except APIError as error:
            print (Fore.RED + error)
            sys.exit()

    def list_containers(self):
        self.client.containers.list()