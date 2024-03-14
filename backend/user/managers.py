from django.contrib.auth.models import UserManager
from datetime import datetime
from django.contrib.auth.models import User

class DiscordUserOAuth2Manager(UserManager):
    def createNewDiscordUser(self, user_data):
        user = User.objects.create_user(username=user_data["username"])
        new_user = self.create(
            user=user,
            userid=user_data["id"],
            username=user_data["username"],
            last_login=datetime.now()
        )
        return new_user

