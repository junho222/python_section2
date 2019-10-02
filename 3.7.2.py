import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class EverytimeText:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add.argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="c:/section3/webdriver/chrome/chromedriver")
        self.driver.implicity(5)

    def ClassEvaluationText(self):
        self.driver.get("")
