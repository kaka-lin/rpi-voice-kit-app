import argparse
import re
import base64
import cv2
import picamera
import sys
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import requests
import fake_chatbot
from gtts import gTTS
from main_chatbot import play_mp3

def takephoto():
    camera = picamera.PiCamera()
    camera.capture('image.jpg')

def main_picamera():
    #takephoto() # First take a picture
    """Run a label request on a single image"""

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open('image.jpg', 'rb') as image:
        # image_content = base64.b64encode(image.read())
        image_content = image.read()
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LOGO_DETECTION',
                    'maxResults': 1
                }]
            }]
        })
        response = service_request.execute()

        try:
             label = response['responses'][0]['logoAnnotations'][0]['description']
        except:
             label = "No response."

        print(label)

def main_img_path(path):
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)


    with open(path, 'rb') as image:
        image_content = (base64.b64encode(image.read())).decode('UTF-8')
        #image_content1 = (image.read()).decode('UTF-8')
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content
                },
                'features': [{
            "type": "LOGO_DETECTION",
            "maxResults": "10"
          },
          {
            "type": "LABEL_DETECTION",
             "maxResults": "10"
          },
          {
            "type": "TEXT_DETECTION",
            "maxResults": "10"
          },
          {
            "type": "WEB_DETECTION",
            "maxResults": "10"
          }

          ]

            }]
        })

        response = service_request.execute()

        try:
             #label = response['responses'][0]['logoAnnotations'][0]['description']
             label = response
        except:
             label = "No response."
        label = str(label)
        delete = "{}[]()/.,-@%&<>'!:;_ "
        for char in delete:
            label=label.replace(char,"")
        label = label.lower()
        #print(label)
        #print()
        count = [0,0,0,0,0]

        brand = ["50lan","coco","comebuy","yifan","tptea"]
        brand_return = ["50嵐", "CoCo", "comebuy", "一芳", "茶湯會"]
        count[0] = label.count("五十嵐")+label.count("50嵐")
        count[1] = label.count("coco")+label.count("都可")
        count[2] = label.count("comebuy")
        count[3] = label.count("一芳")
        count[4] = label.count("tptea")+label.count("茶湯會")+label.count("觀音拿鐵")
        print(count)
        print(brand[count.index(max(count))])
        brand = brand_return[count.index(max(count))]
        brand = "這是{}".format(brand)
        tts = gTTS(brand, lang='zh-tw')
        tts.save('img_brand.mp3')
        play_mp3('img_brand.mp3')

        answer = fake_chatbot.chatbot(brand)
        print(answer)
        tts = gTTS(answer, lang='zh-tw')
        tts.save('img_answer.mp3')
        play_mp3('img_answer.mp3')

if __name__ == '__main__':
    main_img_path(sys.argv[1])
    '''
    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        ret, frame = camera.read()


        if ret:
            cv2.imshow("s",frame)
            main_img_path(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    camera.release()
    cv2.destroyAllWindows()
    '''
