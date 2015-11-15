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
files = open('frames/frames_320.jpg', 'rb').read()

r = requests.post(url, data=files, headers=headers)

response = json.JSONDecoder().decode(r.text)
totals = {}
faces = 0
for key in response:
    faces += 1
    for emotion in key['scores']:
        if faces == 1:
            totals[emotion] = key['scores'][emotion]
        else:
            totals[emotion] += key['scores'][emotion]
            
print(totals)
for emotion in totals:
    print(emotion + ' average: ' + str(totals[emotion] / faces))