from django.urls import path
from .views import discordLogin, discordLoginRedirect, get_authenticated_user

urlpatterns = [
    path("login/", view=discordLogin, name="discord login"),
    path("user/", view=get_authenticated_user, name="authenticated"),
    path("login/redirect/", view=discordLoginRedirect, name="redirect")
]