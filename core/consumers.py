import base64
import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
from core.models import ImageData
import os


class ImageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        image_data = text_data_json['imageB64']
        if ',' in image_data:
            header, image_data = image_data.split(',', 1)
        image_decoded = base64.b64decode(image_data)
        file_name = f'image_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpeg'

        if not os.path.exists('images'):
            os.makedirs('images')
        image_path = os.path.join('images', file_name)
        with open(image_path, 'wb') as image_file:
            image_file.write(image_decoded)

        model_instance = ImageData()
        model_instance.image_data = image_decoded
        model_instance.image_path = image_path

        await database_sync_to_async(model_instance.save)()

        await self.send(text_data=json.dumps({
            'message': f'Image received and saved as {file_name}'
        }))
