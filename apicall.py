import requests
import json

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'e161d0e1d12c434d8b00949bebc9da60'
}
picture = 'https://s.aolcdn.com/hss/storage/midas/fedc672e42fb3f2457bb4a41321a21e7/200006428/smiling-women.jpg'
url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
data = {
    'url': picture
}
r = requests.post(url, data=json.JSONEncoder().encode(data), headers=headers)

print(r.text)