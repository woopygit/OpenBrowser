from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from typing import Dict, Any, Optional, List, Dict, Union
class OpenBrowser:
    def __init__(self, BrowserWidth: Optional[Union[int, str]] = None, BrowserHeight: Optional[Union[int, str]] = None):
        self.BrowserWidth = str(BrowserWidth) if BrowserWidth is not None and (isinstance(BrowserWidth, int) or BrowserWidth.isdigit()) else "1024"
        self.BrowserHeight = str(BrowserHeight) if BrowserHeight is not None and (isinstance(BrowserHeight, int) or BrowserHeight.isdigit()) else "1024"


    def OpenChrome(self, Headless:[Optional[bool]] = False):
        ChromeOption = webdriver.ChromeOptions()
        ChromeOption.add_experimental_option("excludeSwitches", ['enable-automation'])
        # ChromeOption.add_argument("–lang=it");
        # ChromeOption.add_argument("--start-maximized") #"--window-size=1920,1200"
        if Headless == True:
            ChromeOption.add_argument("--headless")
        # ChromeOption.add_argument("--user-data-dir=test")
        ChromeOption.add_argument("disable-infobars")
        ChromeOption.add_argument("--disable-extensions")
        ChromeOption.add_argument("--disable-dev-shm-usage")
        ChromeOption.add_argument("--no-sandbox")
        # ChromeOption.add_argument(("--window-size=820,1080"))
        ChromeOption.add_argument((f"--window-size={self.BrowserWidth},{self.BrowserHeight}"))
        ChromeOption.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        # webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ChromeOption)

        return driver