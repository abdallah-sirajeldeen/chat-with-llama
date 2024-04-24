import json
import os

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings

# Assuming the model is loaded as a global variable in a module
from core.apps import model
from core.gpt_model import predict_prompt


class TextConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        # Optional: Add any cleanup logic here if necessary
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Get prediction from the GPT model
        response = await self.get_prediction(message)
        print(response)


        # Send the model's response back to the client
        await self.send(text_data=json.dumps({
            'response': response
        }))

    @database_sync_to_async
    def get_prediction(self, input_text):
        # Ensure this function is thread-safe and does not manipulate shared states
        output = predict_prompt(input_text)
        return output

    # Ensure that you're handling errors and exceptions appropriately
    async def handle_exception(self, e):
        error_message = str(e)
        await self.send(text_data=json.dumps({'error': error_message}))
