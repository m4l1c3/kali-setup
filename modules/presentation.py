from modules.console_colors import ColorFormatter

class Presentation(object):
    def __init__(self):
        self.color_formatter = ColorFormatter()
        return
    def print_color(self, output):
        print(self.color_formatter.colored(output, 'cyan'))

    def print_footer(self):
        print('\n')
        self.print_color(self.get_seperator())
        self.print_color(self.get_footer())
        self.print_color(self.get_seperator())

    def print_header(self, version):
        self.print_color(self.get_seperator())
        self.print_color(self.get_banner())
        self.print_color(self.get_seperator())
        self.print_color(self.get_version(version))


    @staticmethod
    def get_version(version):
        return '\nVersion: ' + version + '\n'

    @staticmethod
    def get_seperator():
        return '**************************************************************'

    @staticmethod
    def get_footer():
        footer = '*            https://github.com/m4l1c3/kali-setup            *'
        return footer

    @staticmethod
    def get_banner():
        banner = "*                           kali-setup                     *"
        # banner = "* <-.(`-') (`-')  _            _          (`-').->(`-')  _(`-')                 _  (`-') *"
        # banner += "*  __( OO) (OO ).-/    <-.    (_)         ( OO)_  ( OO).-/( OO).->       .->    \-.(OO )  *"
        # banner += "*  '-'. ,--./ ,---.   ,--. )   ,-(`-')    (_)--\_)(,------./    '._  ,--.(,--.   _.'    \ *"
        # banner += "*  |  .'   /| \ /`.\  |  (`-') | ( OO)    /    _ / |  .---'|'--...__)|  | |(`-')(_...--'' *" 
        # banner += "*  |      /)'-'|_.' | |  |OO ) |  |  )    \_..`--.(|  '--. `--.  .--'|  | |(OO )|  |_.' | *"
        # banner += "*  |  .   '(|  .-.  |(|  '__ |(|  |_/     .-._)   \|  .--'    |  |   |  | | |  \|  .___.' *"
        # banner += "*  |  |\   \|  | |  | |     |' |  |'->    \       /|  `---.   |  |   \  '-'(_ .'|  |      *"
        # banner += "*  `--' '--'`--' `--' `-----'  `--'        `-----' `------'   `--'    `-----'   `--'      *"
        return banner
