import requests

response = requests.get("https://en.wikipedia.org/")
if response.status_code == 200:
    print("Wikipedia Page Found")