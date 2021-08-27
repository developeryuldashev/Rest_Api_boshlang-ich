from channels.generic.websocket import WebsocketConsumer
import json
import time
from random import randint
class RTWiew(WebsocketConsumer):
    def connect(self):
        self.accept()
        for i in range(100):
            data=json.dumps({
                # 'number':randint(0,100)
                'number':i
            })
            self.send(data)
            time.sleep(1)