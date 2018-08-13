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
            'properties': ['read', 'write'],
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
        data = int.from_bytes(data, 'little')
        led = aiy.voicehat.get_led()

        if data == 1:
            led.set_state(led.BLINK_3)
            time.sleep(2)
            led.set_state(led.OFF)

        callback(Characteristic.RESULT_SUCCESS)
