import requests
# after
with open("names.txt", "r") as my_file:
    names = my_file.read().splitlines()
    for name in names:
        print(name)

print(my_file)
with requests.get("https://google.com/aiwefdbliasbdfilasbdf") as response:
    response.raise_for_status()