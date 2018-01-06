"""
Logging module
"""
from modules.console_colors import ColorFormatter

class Logger(object):
    """
    Logging object for writing status to command line
    """
    def __init__(self):
        self.color_formatter = ColorFormatter()
        return

    def error(self, output):
        """
        log error message to console
        """
        print self.color_formatter.colored("[*] " + output, "red")

    def warning(self, output):
        """
        log warning to console
        """
        print self.color_formatter.colored("[*] " + output, "yellow")

    def debug(self, output):
        """
        log debug to console
        """
        print self.color_formatter.colored("[*] " + output, "green")

    def normal_output(self, output):
        """
        log normal output
        """
        print self.color_formatter.colored("[*] " + output, "cyan")
