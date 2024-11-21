from selenium import webdriver
from time import sleep
d = webdriver.Chrome()
def my_test(values_to_check, expected):
    d.get("file:///Users/aviel.buskila/Downloads/tip_calc%202/index.html")
    d.find_element(by="id", value="billamt").send_keys(values_to_check[0])
    d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
    d.find_element(by="id", value="peopleamt").send_keys(values_to_check[1])
    d.find_element(by="id", value="musicamt").send_keys(values_to_check[2])
    d.find_element(by="id", value="calculate").click()
    actual = d.find_element(by="id", value="tip").text
    is_visible = d.find_element(by="id", value="tip").is_displayed()
    assert actual == expected
    assert is_visible


my_test(["100", "5", "2"], "6.00")
my_test(["100", "4", "1"], "6.00")
