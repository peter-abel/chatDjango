# myapp/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from .tasks import process_user_message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        user_message = text_data
        await self.send(text_data=json.dumps({'message': user_message, 'status': 'User message received'}))

        # Process the user message asynchronously
        process_user_message.delay(self.channel_name, user_message)

    async def chat_message(self, event):
        bot_response = event['message']
        await self.send(text_data=json.dumps({'message': bot_response, 'status': event['status']}))

