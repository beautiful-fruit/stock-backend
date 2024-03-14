from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

import requests

@login_required(login_url="/oauth/login")
def get_authenticated_user(request):
    return JsonResponse({"user": "authenticated"})

def discordLogin(request: HttpRequest) -> HttpResponseRedirect:
    return redirect(settings.AUTH_URL_DISCORD)

def discordLoginRedirect(request: HttpRequest) -> JsonResponse:
    code = request.GET.get("code")
    user_data = exchange_code(code)
    discord_user = authenticate(request, user_data=user_data)
    login(request, discord_user)
    return redirect("http://localhost:8000/oauth/user")

def exchange_code(code: str):
    data = {
        "client_id": settings.CLIENT_ID, 
        "client_secret": settings.CLIENT_SECRET,
        "grant_type": "client_credentials",
        "code": code,
        "redirect_uri": settings.REDIRECT_URI,
        "scope": "identify connections",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"     
    }
    
    response = requests.post(settings.TOKEN_URL, data=data, headers=headers)
    credentials = response.json()
    access_token = credentials["access_token"]
    
    response = requests.get(
        settings.USER_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    
    user_data = response.json()
    
    return user_data
        
    