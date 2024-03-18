from django.urls import path
from .views import discordLogin, discordLoginRedirect

urlpatterns = [
    path("login/", view=discordLogin, name="discord login"),
    path("login/redirect/", view=discordLoginRedirect, name="redirect")
]