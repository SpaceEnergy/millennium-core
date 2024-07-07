import Millennium
import configparser, os

class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_file = os.path.join(Millennium.steam_path(), "ext", "millennium.conf")

        if os.path.exists(self.config_file):
            try:
                self.config.read(self.config_file)
            except configparser.Error:
                print("error reading config file, resetting...")

        self.setup()

    def set_default(self, section, key, value):

        if section not in self.config:
            self.config[section] = {}

        if key not in self.config[section]:
            self.config[section][key] = value

    def get(self, section, key):
        return self.config[section][key]

    def setup(self):

        LOCALS = os.path.join(Millennium.steam_path(), "ext", "data")

        PYTHON_BIN       = os.path.join(LOCALS, "cache", "python.exe")
        PACMAN_LOGS      = os.path.join(LOCALS, "logs", "pacman.log")
        PIP_INSTALL_LOGS = os.path.join(LOCALS, "logs", "pip_boot.log")

        self.set_default('package.manager', 'devtools', 'no')
        self.set_default('package.manager', 'auto_update_devtools', 'yes')
        self.set_default('package.manager', 'use_pip', 'yes')
        self.set_default('package.manager', 'python', PYTHON_BIN)
        self.set_default('package.manager', 'pip_logs', PACMAN_LOGS)
        self.set_default('package.manager', 'pip_boot', PIP_INSTALL_LOGS)

        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)