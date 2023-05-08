import platform
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceC
from selenium.webdriver.firefox.service import Service as ServiceF
from selenium.webdriver.edge.service import Service as ServiceE
from selenium.webdriver.chrome.options import Options as OptionsC
from selenium.webdriver.firefox.options import Options as OptionsF



class Device:
    def __init__(self, os_info, version):
        self.os_info, self.version = os_info, version
        self._chromedriver_path = self._get_path(
            "drivers", self.os_info, "chromedriver"
        )
        self._geckodriver_path = self._get_path("drivers", self.os_info, "geckodriver")
        self._msedgedriver_path = self._get_path(
            "drivers", self.os_info, "msedgedriver"
        )
        self.txt_results_path = self._get_path(
            "results",
            self.os_info + " " + self.version,
            "comparisons",
            create_if_not_exist=True,
        )
        self.comparison_json_path = self._get_path(
            "results", self.os_info + " " + self.version, "comparisons.json"
        )
        self.doms_json_path = self._get_path(
            "results", self.os_info + " " + self.version, "doms.json"
        )

    def _get_path(self, *dirs: str, create_if_not_exist: bool = False):
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, *dirs)
        if create_if_not_exist is True and not os.path.exists(path):
            os.makedirs(path)
        return path

    def _get_os_info(self):
        system = platform.system()
        if system == "Windows":
            return "windows", platform.release()
        elif system == "Darwin":
            return "macos", platform.mac_ver()[0]
        elif system == "Linux":
            return "linux", platform.linux_distribution()[0]

    def chrome(self) -> webdriver.Chrome:
        return webdriver.Chrome(service=ServiceC(self._chromedriver_path))

    def _get_brave_path(self):
        if self.os_info == "windows":
            return "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        elif self.os_info == "macos":
            return "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        elif self.os_info == "linux":
            return "/usr/bin/brave-browser"
        else:
            return None

    def brave(self) -> webdriver.Chrome:
        options = OptionsC()
        options.binary_location = (
            self._get_brave_path()
        )  # modify it so that it points to the brave executable, shell command for linux: which brave
        return webdriver.Chrome(
            service=ServiceC(self._chromedriver_path), options=options
        )

    def firefox(self) -> webdriver.Firefox:
        if self.os_info == "windows":
            optionsf = OptionsF()
            optionsf.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
            return webdriver.Firefox(service=ServiceF(self._geckodriver_path), options=optionsf)
        else:
            return webdriver.Firefox(service=ServiceF(self._geckodriver_path))

    def safari(self) -> webdriver.Safari:
        # Remove below command if it is the first time and macos
        # os.system("safaridriver --enable")
        return webdriver.Safari()

    def edge(self) -> webdriver.Edge:
        return webdriver.Edge(service=ServiceE(self._msedgedriver_path))