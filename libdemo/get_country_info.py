import requests

code = input("Enter country code :")
resp = requests.get("https://restcountries.eu/rest/v2/alpha/" + code)
info = resp.json()
if 'name' in info:
    print(info["name"])
    print(info["capital"])
else:
    print("Country Not Found!")


