from django.conf import settings

import requests
from typing import Dict
from icecream import ic # Debug

def exchange_code(code: str) -> Dict | None:
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.REDIRECT_URI,
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(settings.TOKEN_URL, data=data, headers=headers)
    if response.status_code != 200:
        ic()
        return None
    
    credentials = response.json()
    ic(credentials)
    if "identify" not in credentials["scope"] or "email" not in credentials["scope"]:
        ic()
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

def refresh_token(refresh_token: str) -> Dict | None:
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(settings.TOKEN_URL, data=data, headers=headers)
    if response.status_code != 200:
        ic()
        return None
    
    credentials = response.json()
    ic(credentials)
    if "identify" not in credentials["scope"] or "email" not in credentials["scope"]:
        ic()
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

ic.disable()