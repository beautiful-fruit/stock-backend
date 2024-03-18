from django.db import models

# Create your models here.

class DiscordUser(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    globalname = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    
    def __str__(self) -> str:
        return f"{self.username}"
    
