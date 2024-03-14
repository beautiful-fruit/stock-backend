from typing import Dict
from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest

from user.models import DiscordUser


class DiscordBackend(BaseBackend):
    def authenticate(self, request: HttpRequest, user_data):
        if not DiscordUser.objects.filter(userid=user_data['id']).exists():
            new_user = DiscordUser.objects.createNewDiscordUser(user_data)
            return new_user
        return DiscordUser.objects.get(userid=user_data['id'])
    
    def get_user(self, user_id: int):
        if not DiscordUser.objects.filter(pk=user_id).exists():
            return None
        return DiscordUser.objects.get(pk=user_id)
        