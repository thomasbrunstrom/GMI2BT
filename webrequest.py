from PIL import Image
import requests
import json

def fetchUrl(url):
    response = requests.get(url)
    data = response.text
    try:
        with open('file.html', 'w') as fpointer:
            fpointer.write(data)
    except FileNotFoundError as ferr:
        print(ferr)

fetchUrl('https://www.google.com/')