from selenium import webdriver
from time import sleep
dd = webdriver.Chrome()

dd.get("https://github.com")
sleep(10)