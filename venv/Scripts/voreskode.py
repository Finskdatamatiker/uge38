import requests

forside = requests.get('http://www.kea.dk',allow_redirects = True)
result = forside.text
print(result)

