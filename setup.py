"""
Main runtime class, runs all the setup commands
"""

from multiprocessing.dummy import Pool as ThreadPool
from termcolor import colored
from modules.logger import Logger
from modules.presentation import Presentation

class KaliSetup(object):
    def __init__(self):
	self.thread_pool = ThreadPool(4)
	self.version = '0.0.1'
        self.presentation = Presentation()
	self.website = 'https://github.com/m4l1c3/kali-setup'
        self.presentation.print_header(self.version)
        self.presentation.print_footer()
 
   # def get_assets(self):
   #     return

   # def get_tasks(self):
   #     return {

   #      }

KaliSetup()
