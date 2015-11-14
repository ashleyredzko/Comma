import requests
import json

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'e161d0e1d12c434d8b00949bebc9da60'
}

picture = 'https://theparentescape.files.wordpress.com/2015/10/prevention-image-of-large-group-smiling-300x200.jpg'

data = {
    'url': picture
}

url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
files = {'files': open('example.jpg', 'rb').read() }

r = requests.post(url, data=files, headers=headers)

print(r.text)