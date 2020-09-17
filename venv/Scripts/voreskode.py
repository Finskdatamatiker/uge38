import requests

forside = requests.get('http://www.kea.dk',allow_redirects = True)
result = forside.text
print(result)

request_from_kea = requests.get('https://kea.dk/images/resources/logo-main-black-single.png', allow_redirects = True)

with open('kea_image.png', 'wb') as picture:
    picture.write(request_from_kea.content)