"""
Color formatting
"""

class Colors(object):
    """
    Color format ansi codes
    """
    NORMAL = ""
    INFO = "\033[94m"
    SUCCESS = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"

    def __init__(self):
        return

class ColorFormatter(object):
    """
    Output for Colors
    """
    def __init__(self):
        return

    def colored(self, message, color_type):
        """
        return formatted message for coloring
        """
        color = self.get_color(color_type)
        return color + message  + Colors.ENDC

    @staticmethod
    def get_color(color_type):
        """
        return color replace string
        """
        if color_type == "cyan":
            return Colors.INFO
        elif color_type == "yellow":
            return Colors.WARNING
        elif color_type == "green":
            return Colors.SUCCESS
        elif color_type == "red":
            return Colors.FAIL
        return Colors.NORMAL
