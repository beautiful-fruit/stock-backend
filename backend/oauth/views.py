from django.shortcuts import redirect
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login

from .schemas import DiscordUserBase
from .auth import authentucate
from .discord_oauth import exchange_code, refresh_token
import json


def discordLogin(request: HttpRequest) -> HttpResponseRedirect:
    return redirect(settings.AUTH_URL_DISCORD)


def discordLoginRedirect(request: HttpRequest) -> JsonResponse:
    code = request.GET.get("code")
    data = exchange_code(code)
    if data is None:
        response = json.dumps({"message": "Authorize Failed"})
        return HttpResponse(response, content_type="application/json", status=401)
    user_data = DiscordUserBase(**data)
    user = authentucate(user_data)
    if user is None:
        response = json.dumps({"message": "Email is not Verified"})
        return HttpResponse(response, content_type="application/json", status=401)
    
    if user == "refresh":
        refresh_data = refresh_token(code)
        if refresh_data is None:
            response = json.dumps({"message": "Authorize Failed"})
            return HttpResponse(response, content_type="application/json", status=401)
        user_data = DiscordUserBase(**data)
        user = User.objects.get(username=user_data.id)
        login(request, user)
        return redirect("http://localhost:8000/user")
    
    
    login(request, user)
    response = json.dumps({"message": "Create User Success"})
    return HttpResponse(response, content_type="application/json", status=201)



