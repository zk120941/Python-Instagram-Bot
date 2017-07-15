from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import paramiko
import threading
import getpass
import random
import os
from shutil import copyfile
import re
import time
import requests
from random import randint


class Instagram:

    def __init__(self, u, p, msg):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome("C:\Users\Gas_Sales\AppData\Local\Temp\Temp1_chromedriver_win32.zip\chromedriver.exe") #path to chromedriver.exe

        self.username = u
        self.password = p
        self.msgs = msg

    def login(self):
        self.browser.get("https://instagram.com/accounts/login/?force_classic_login")
        self.browser.find_element_by_name("username").send_keys(self.username)
        self.browser.find_element_by_name("password").send_keys(self.password)
        self.browser.find_element_by_name("password").send_keys(u'\ue007')

        time.sleep(5)
        if "force_classic_login" in self.browser.current_url:
            return False
        return True

    def search_for_keyword(self, tag):
        self.browser.get("https://www.instagram.com/explore/tags/" + tag)
        links = self.browser.find_elements_by_css_selector("a")
        urls = []
        for link in links:
            urls.append(link.get_attribute("href"))

        index = 0
        for url in urls:
            index = index + 1
            self.browser.get(url)
            self.comment(self.get_comment())
            if index%25 == 0: # initiate delay every 25 minutes
                time.sleep(8 * 60) # ^ pause for 8 minutes
            else:
                time.sleep(20) # delay after every comment in seconds (default 20)

    def get_comment(self):
        with open(self.msgs) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        return random.choice(content)
        

    def comment(self, comment):
        self.browser.find_element_by_css_selector("textarea").send_keys(comment)
        self.browser.find_element_by_css_selector("textarea").send_keys(u'\ue007')
        


if __name__ == "__main__":
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    message = raw_input("Enter comment list file name (example.txt): ")
    ig = Instagram(username, password, message)
    is_logged_in = ig.login()
    if not is_logged_in:
        print("Wrong username and/or password.")
        sys.exit(0)
    tag_keyword = raw_input("What tag should we search for: ")
    ig.search_for_keyword(tag_keyword)
