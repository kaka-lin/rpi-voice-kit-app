import sys

from pybleno import *
from rpi_service import *

bleno = Bleno()

primaryService = RpiService()

def onStateChange(state):
    print('on -> stateChange: ' + state)

    if (state == 'poweredOn'):
        bleno.startAdvertising('Kaka RPi3', [primaryService.uuid])
    else:
        bleno.stopAdvertising()

bleno.on('stateChange', onStateChange)

def onAdvertisingStart(error):
    print('on -> advertisingStart: ' + ('error ' + error if error else 'success'))

    if not error:
        def on_setServiceError(error):
            print('setServices: %s'  % ('error ' + error if error else 'success'))

        bleno.setServices([
            primaryService
        ], on_setServiceError)

bleno.on('advertisingStart', onAdvertisingStart)

print('Hit <Enter> to disconnect')

if (sys.version_info > (3, 0)):
    input()
else:
    raw_input()

bleno.stopAdvertising()
bleno.disconnect()

print ('terminated.')
sys.exit(1)
