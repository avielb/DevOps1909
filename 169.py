import requests
from time import sleep
try:
    response = requests.get('https://kajdsfkasdf')
except ZeroDivisionError:
    print("Divide by zero")
except ValueError:
    print("Value Error")
except BaseException as moshe:
    print(f"something went wrong: {moshe.args}")

time_to_sleep = input("time_to_sleep: ")
sleep(time_to_sleep)
a = int(input("first: "))
b = int(input("second: "))
res = (a / b)
print(res)