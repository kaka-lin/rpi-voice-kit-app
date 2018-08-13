from pybleno import *
from aiy_characteristic import *

class RpiService(BlenoPrimaryService):
    def __init__(self):
        BlenoPrimaryService.__init__(self, {
            'uuid': '11111111111111111111111111111117',
            'characteristics': [
                AiyCharacteristic()
            ]
        })
