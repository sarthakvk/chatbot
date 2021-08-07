import json
from channels.generic.websocket import WebsocketConsumer
from chat.views import respond_to_websockets
from .models import ButtonCalls

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        joke_type = text_data_json['text']

        if joke_type in ["dumb", "stupid", "fat"]:
            user = self.scope["user"]
            if not user.is_anonymous:
                bc, _ = ButtonCalls.objects.get_or_create(user=user)
            else:
                bc, _ = ButtonCalls.objects.get_or_create(user=None)
            if joke_type == "fat":
                bc.fat_count += 1
            elif joke_type == "stupid":
                bc.stupid_count += 1
            else:
                bc.dumb_count += 1
            bc.save()

        self.send(text_data=json.dumps({
            'message': respond_to_websockets(joke_type)
        }))