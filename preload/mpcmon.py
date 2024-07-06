import importlib
import json
import subprocess
import urllib.request, urllib.error

class mpc:

    def __init__(self, m_python_bin):
        self.__python_bin = m_python_bin

    def get_live_version(self):
        try:
            url = "https://pypi.org/pypi/millennium/json"
            response = urllib.request.urlopen(url)
            return json.load(response)["info"]["version"]

        except urllib.error.URLError as e:
            print(f"could not connect to pypi.org {e.reason}")
            return None

    def update_millennium(self):
        print("updating millennium dev tools...")
        subprocess.run([self.__python_bin, "-m", "pip", "install", "--upgrade", "millennium"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def start(self, config):
        if (config.get('package.manager', 'devtools') != 'yes'):
            print("millennium dev tools are disabled")
            return

        try:
            if config.get('package.manager', 'auto_update_devtools') == 'no':
                print("millennium dev tools auto update is disabled")
                return

            if self.get_live_version() != importlib.metadata.version("millennium"):
                self.update_millennium()
            else:
                print("millennium dev tools are up to date")
                
        except importlib.metadata.PackageNotFoundError as e:
            print("millennium dev tools are not installed")
            self.update_millennium()