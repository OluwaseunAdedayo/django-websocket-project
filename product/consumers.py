from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ProductConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "product_updates"
        
        # Join group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # You can process client input here if needed
        await self.send(text_data=f"Echo: {text_data}")

    async def product_message(self, event):
        # Called when Celery sends to the group
        await self.send(text_data=json.dumps(event["data"]))



