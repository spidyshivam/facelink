import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import ChatMessage
from asgiref.sync import sync_to_async

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = self.scope["url_route"]["kwargs"]["username"]
        self.user = self.scope["user"]

        self.room_name = f"chat_{min(self.user.username, self.username)}_{max(self.user.username, self.username)}"
        self.room_group_name = f"chat_{self.room_name}"

        if self.user.is_authenticated:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """Handles incoming WebSocket messages."""
        data = json.loads(text_data)
        message = data["message"]

        if self.user.is_authenticated:
            other_user = await sync_to_async(User.objects.get)(username=self.username)
            chat_message = await sync_to_async(ChatMessage.objects.create)(
                sender=self.user, receiver=other_user, message=message
            )

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "sender": self.user.username
                }
            )

    async def chat_message(self, event):
        """Sends message to WebSocket."""
        await self.send(text_data=json.dumps(event))
