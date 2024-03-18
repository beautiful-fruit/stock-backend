from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login

from .schemas import DiscordUserBase
from .auth import authentucate
import json
from typing import Dict

import requests


@login_required(login_url="/oauth/login")
def get_authenticated_user(request):
    return JsonResponse({"user": "authenticated"})


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
    login(request, user)
    response = json.dumps({"message": "Create User Success"})
    return HttpResponse(response, content_type="application/json", status=201)


def exchange_code(code: str) -> Dict | None:
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.REDIRECT_URI,
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET
    }

    response = requests.post(settings.TOKEN_URL, data=data)
    if response.status_code != 200:
        return None
    
    credentials = response.json()
    
    if "identify" not in credentials.keys() or "email" not in credentials.keys():
        return None
    
    access_token = credentials["access_token"]

    response = requests.get(
        settings.USER_URL,
        headers={
            "Authorization": f"Bearer {access_token}" 
        }
    )

    user_data = response.json()
    return user_data
