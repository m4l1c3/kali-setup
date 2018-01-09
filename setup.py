"""
Main runtime class, runs all the setup commands
"""

from multiprocessing.dummy import Pool as ThreadPool
from modules.logger import Logger
from modules.presentation import Presentation
from modules.execute_command import ExecuteCommand


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
        self.get_commands()
        self.executioner = ExecuteCommand()
        for command in self.commands:
            print(command)
            self.executioner.execute_command(command)
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
    def get_commands(self):
        """
        get commands to run
        """
        self.commands = []
        # self.commands.append("apt-get update")
        # self.commands.append("network-manager-openvpn network-manager-openvpn-gnome " +
        #                      "network-manager-pptp" +
        #                      "network-manager-pptp-gnome" +
        #                      "network-manager-strongswan network-manager-vpnc " +
        #                      "network-manager-vpnc-gnome")
        self.commands.append("git clone https://github.com/OJ/gobuster.git")
        self.commands.append("git clone https://github.com/jhaddix/domain.git")
        self.commands.append("wget https://dl.google.com/go/go1.9.2.linux-amd64.tar.gz")
        self.commands.append("git clone https://bitbucket.org/LaNMaSteR53/recon-ng.git")
        self.commands.append("mkdir -p ~/burpmodules")
        self.commands.append("git clone https://github.com/bugcrowd/HUNT.git")
        self.commands.append("git clone https://github.com/danielmiessler/SecLists")

KaliSetup()
