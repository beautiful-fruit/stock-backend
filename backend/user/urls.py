from django.urls import path
from .views import get_authenticated_user

urlpatterns = [
    path("", view=get_authenticated_user, name="authenticated"),
]