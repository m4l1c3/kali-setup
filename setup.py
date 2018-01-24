"""
Main runtime class, runs all the setup commands
"""

from multiprocessing.dummy import Pool as ThreadPool
from modules.logger import Logger
from modules.presentation import Presentation
from modules.execute_command import ExecuteCommand
import os
import sys

class KaliSetup(object):
    """
    Setup Object
    """
    def __init__(self):
        self.thread_pool = ThreadPool(4)
        self.version = '0.0.1'
        self.presentation = Presentation()
        self.website = 'https://github.com/m4l1c3/kali-setup'
        self.presentation.print_header(self.version)
        self.presentation.print_footer()
        self.basedir = "/opt"
        self.logger = Logger()
        self.get_commands()
        self.setup_go()
        self.get_gobuster()
        self.setup_domain()
        self.setup_discover()
        self.extract_rockyou()
        self.setup_reconng()
        self.setup_burpmodules()
        self.get_linenum()
        self.executioner = ExecuteCommand()
        for command in self.commands:
            self.executioner.execute_command(command)
        # install vmware tools
        #install golang
        #clone gobuster
        #enable ssh?
        #linenum?
        #privesccheck?
        #guake?
        #burp pro?
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
        self.commands.append("mkdir -p " + self.basedir)
        #  self.get_apt_commands()

    def setup_burpmodules(self):
        if not os.path.exists(self.basedir + "/burpmodules"):
            self.commands.append("mkdir -p " + self.basedir + "/burpmodules")
        if not os.path.exists(self.basedir + "/burpmodules/HUNT"):
            self.commands.append("git clone https://github.com/bugcrowd/HUNT.git " + self.basedir
                            + "/burpmodules/HUNT")

    def get_seclists(self):
        if not os.path.exists(self.basedir + "/SecLists"):
            self.commands.append("git clone https://github.com/danielmiessler/SecLists " + self.basedir + "/SecLists")

    def setup_domain(self):
        if not os.path.exists(self.basedir + "/domain"):
            self.commands.append("git clone https://github.com/jhaddix/domain.git " + self.basedir + "/domain")
    
    def setup_reconng(self):
        if not os.path.exists(self.basedir + "/recon-ng"):
            self.commands.append("git clone https://bitbucket.org/LaNMaSteR53/recon-ng.git " + self.basedir + "/recon-ng")

    def get_apt_commands(self):
        self.commands.append("apt-get update")
        self.commands.append("apt-get install -y open-vm-tools network-manager-openvpn network-manager-openvpn-gnome " +
                             "network-manager-pptp network-manager-pptp-gnome network-manager-strongswan " + 
                             "network-manager-vpnc network-manager-vpnc-gnome neovim")
        self.commands.append("apt-get -y dist-upgrade")
    
    def get_linenum(self):
        if not os.path.exists(self.basedir + "/linenum"):
            self.commands.append("git clone https://github.com/rebootuser/LinEnum.git " + self.basedir + "/linenum")

    def setup_go(self):
        """
        setup golang
        """
        if not os.path.exists("/usr/local/go"):
            self.commands.append("wget https://dl.google.com/go/go1.9.2.linux-amd64.tar.gz")
            self.commands.append("tar -C /usr/local -zxvf go1.9.2.linux-amd64.tar.gz")
        if "/usr/local/go" not in sys.path:
            self.commands.append("echo 'PATH=$PATH:/usr/local/go/bin' >> ~/.profile")

        if not os.path.exists("/usr/local/go"):
            self.logger.error("Unable to find installed go directory")

    def get_gobuster(self):
        """
        setup gobuster
        """
        if not os.path.exists(self.basedir + '/gobuster'):
            self.commands.append("git clone https://github.com/OJ/gobuster.git " + self.basedir + "/gobuster")
        if os.path.exists(self.basedir + '/gobuster'): 
            self.commands.append("cd " + self.basedir + "/gobuster && go get && go build && go install")
            self.commands.append("alias gobuster='go run " + self.basedir + "/gobuster/main.go")
        else:
            self.logger.error("Unable to find gobuster directory")
    def get_discover(self):
        """
        setup discover framework
        """
        if not os.path.exists(self.basedir + "/discover"):
            self.commands.append("git clone https://github.com/leebaird/discover " + self.basedir + "/discover")
    
    def extract_rockyou(self):
        """
        extract built-in rockyou in kali
        """
        if not os.path.exists("/usr/share/wordlists/rockyou.txt") and os.path.exists("/usr/share/wordlists/rockyou.txt.gz"):
            self.commands.append("gzip -d /usr/share/wordlists/rockyou.txt.gz")
KaliSetup()
