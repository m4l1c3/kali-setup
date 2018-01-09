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

    logger = Logger()

    def __init__(self):
        return

    def execute_command(self, command_text):
        """
        Execute a command using subprocess.check_output
        """
        try:
            return subprocess.Popen(command_text.split(" "), stdout=subprocess.PIPE)
        except (OSError, CalledProcessError) as error:
            self.logger.error("Error processing command: " + command_text + " " + error.output)
            return

    def thing(self):
        """
        test
        """
        return self
