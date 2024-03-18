from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse

# Create your views here.

@login_required(login_url="/oauth/login")
def get_authenticated_user(request: HttpRequest):
    print(request.user)
    return JsonResponse({"user": "authenticated"})
