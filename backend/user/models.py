from django.db import models
from django.contrib.auth.models import User

from user.managers import DiscordUserOAuth2Manager


class DiscordUser(models.Model):

    objects = DiscordUserOAuth2Manager()

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    userid = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    last_login = models.DateTimeField(null=True, blank=True)
    
    def is_authenticated(self, request):
        return True
    
