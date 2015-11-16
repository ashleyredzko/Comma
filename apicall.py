import requests
import json
import os
import time

totals = {}
faces = 0

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '<insert Project Oxford Emotion API key here>'
}

url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'



file_list = os.listdir('frames/')

for filename in file_list:
    files = open('frames/' + filename, 'rb').read()
    print('Processing ' + filename + '...')
    r = requests.post(url, data=files, headers=headers)

    response = r.json()

    time.sleep(2)
    
    responses = open('responses.txt', 'a')
    
    responses.write(r.text)
    
    responses.close()

    for key in response:
        faces += 1
        for emotion in key['scores']:
            if faces == 1:
                totals[emotion] = key['scores'][emotion]
            else:
                totals[emotion] += key['scores'][emotion]
         
responses = open('responses.txt', 'a')

for emotion in totals:
    average = emotion + ' average: ' + str(totals[emotion] / faces)
    print(average)
    responses.write(average)
    
responses.close()
