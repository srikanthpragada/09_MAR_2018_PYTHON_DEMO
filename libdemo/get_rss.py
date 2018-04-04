import requests

r = requests.get('http://www.srikanthtechnologies.com/rss.xml')
if r.status_code == 200:
    print(r.text)
else:
    print("Sorry! URL Not found!")