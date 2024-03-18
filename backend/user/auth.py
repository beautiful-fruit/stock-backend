from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .schemas import DiscordUserBase
from .models import DiscordUser

def authentucate(data: DiscordUserBase) -> User | None:
    
    if not data.verified:
        return None
    if User.objects.filter(username=data.id).exists():
        return User.objects.get(username=data.id)
    
    new_user = User.objects.create_user(
        username=data.id,
        email=data.email,
        password=make_password(data.username)
    )
    new_user.save()
    
    discord_user = DiscordUser.objects.create(
        userid=data.id,
        username=data.username,
        avatar=data.avatar,
        globalname=data.global_name,
        email=data.email
    )
    discord_user.save()
    
    return new_user
        