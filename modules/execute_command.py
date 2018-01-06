"""
Command execution module
"""

from subprocess import CalledProcessError
from subprocess import check_output
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
            return check_output(command_text.split(" "))
        except (OSError, CalledProcessError) as error:
            self.logger.error("Error processing command: " + command_text + " " + error.output)
            return

    def thing(self):
        """
        test
        """
        return self
