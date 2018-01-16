"""
Command execution module
"""

from subprocess import CalledProcessError
import subprocess
from modules.logger import Logger

class ExecuteCommand(object):
    """
    Command execution object
    """
    def __init__(self):
        self.logger = Logger()

    def execute_command(self, command_text):
        """
        Execute a command using subprocess.check_output
        """
        self.logger.normal_output(command_text)
        try:
            return subprocess.check_output(command_text.split(" "))
        except (OSError, CalledProcessError) as error:
            self.logger.error("Error processing command: " + command_text + " " + error.output)
            return

    def thing(self):
        """
        test
        """
        return self
