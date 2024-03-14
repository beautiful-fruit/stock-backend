from django.contrib import admin

from .models import DiscordUser
# Register your models here.
@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    """
    Register DiscordUser model to admin site.
    """

    list_display = (
        "userid",
        "username",
        "last_login",
    )
