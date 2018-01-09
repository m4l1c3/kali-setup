"""
Main runtime class, runs all the setup commands
"""

from multiprocessing.dummy import Pool as ThreadPool
from modules.logger import Logger
from modules.presentation import Presentation

class KaliSetup(object):
    """
    Setup Object
    """
    logger = Logger()
    def __init__(self):
        self.thread_pool = ThreadPool(4)
        self.version = '0.0.1'
        self.presentation = Presentation()
        self.website = 'https://github.com/m4l1c3/kali-setup'
        self.presentation.print_header(self.version)
        self.presentation.print_footer()
        # install vmware tools
        # install git?
        #install golang
        #clone gobuster
        #clone haddix domain
        #install openvpn
        #enable ssh?
        #clone seclists
        #linenum?
        #privesccheck?
        #guake?
        #burp pro?
        #python 3?
        #pip3?
        #clone hunt methodology
    def get_assets(self):
        """
        Get assets
        """
        return self
    def get_tasks(self):
        """
        Get tasks
        """
        return self

KaliSetup()
