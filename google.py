
import time
from selenium import webdriver
import pickle


browser = webdriver.Chrome("/home/vacha320/chromedriver")
browser.get("https://freebitco.in/?op=home")
# pickle.dump(browser.get_cookies(), open("session", "wb"))
for cookie in pickle.load(open("session", "rb")):
    browser.add_cookie(cookie)

browser.get("https://freebitco.in/?op=home")
browser.refresh()
time.sleep(10)
