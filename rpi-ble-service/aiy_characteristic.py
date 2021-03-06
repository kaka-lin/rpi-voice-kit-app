import time
import array
import subprocess

from pybleno import *
import aiy.audio
import aiy.voicehat

class AiyCharacteristic(Characteristic):
    def __init__(self):
        Characteristic.__init__(self, {
            'uuid': '11111111111111111111111111111001',
            'properties': ['read', 'writeWithoutResponse'],
            'descriptors': [
                Descriptor(
                    uuid = '2901',
                    value = 'Gets or sets the action of voice kit'
                ),
            ],
            'value': None
        })

    def onReadRequest(self, offset, callback):
        try:
            output = subprocess.check_output(['ls'])
            print('test', output)
        except subprocess.CalledProcessError:
            print('Exception handled')

        #callback(Characteristic.RESULT_SUCCESS, bytearray([10]))
        callback(Characteristic.RESULT_SUCCESS, array.array('B', [10]))

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        #data = int.from_bytes(data, 'little')
        data = data.decode('utf-8')
        print("Receive: {}".format(data))
        led = aiy.voicehat.get_led()

        if data == "Voice Kit Led test":
            led.set_state(led.BLINK_3)
            time.sleep(2)
            led.set_state(led.OFF)
        elif data == "Voice Kit Audio test":
            cmd = 'gnome-terminal -e "python3 /home/pi/AIY-projects-python/checkpoints/check_audio.py"'
            p = subprocess.Popen(cmd, shell=True)
        elif data == "ekko start":
            cmd = "python3 /home/pi/rpi-app/rpi-chatbot-2/main_chatbot.py"
            p = subprocess.Popen(cmd, shell=True)
        elif data == "ekko image start":
            cmd = " export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/VisionPixnet-2f48128dc198.json; python3 /home/pi/rpi-app/rpi-chatbot-2/image.py /home/pi/rpi-app/rpi-chatbot-2/data/image.jpg"
            p = subprocess.Popen(cmd, shell=True)
        else:
            pass

        callback(Characteristic.RESULT_SUCCESS)
