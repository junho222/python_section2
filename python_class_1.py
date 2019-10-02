import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("------------")

user1 = UserInfo()
user2 = UserInfo()

user1.set_info('kim', '010-3323-0922')
user2.set_info('park', '010-2729-6672')

user1.print_info()
user2.print_info()


print(user1.__dict__)
print(user2.__dict___)
