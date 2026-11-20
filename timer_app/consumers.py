import json
import time
from channels.generic.websocket import AsyncWebsocketConsumer

STATE = {'running': False, 'end_time': 0}

class TimerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('timer_group', self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({'action': 'sync', **STATE}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('timer_group', self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        
        if data['action'] == 'start':
            STATE['running'] = True
            STATE['end_time'] = int(time.time() * 1000) + data['duration']
        elif data['action'] == 'stop':
            STATE['running'] = False
            STATE['end_time'] = 0

        await self.channel_layer.group_send(
            'timer_group',
            {'type': 'timer_msg', 'data': {'action': data['action'], **STATE}}
        )

    async def timer_msg(self, event):
        await self.send(text_data=json.dumps(event['data']))