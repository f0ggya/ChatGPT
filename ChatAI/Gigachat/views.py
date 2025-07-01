from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import requests, json
from .models import *


def home(request):
    if request.user.is_authenticated:
        if not Setting.objects.filter(owner=request.user):
            Setting.objects.create(theme='light_theme', owner=request.user)
        return render(request, 'base.html')
    return render(request, 'home.html')


@require_http_methods(['POST'])
@csrf_exempt
def send_message(request):
    data = json.loads(request.body)
    prompt = data['prompt']
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload={
    'scope': 'GIGACHAT_API_PERS'
    }
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': '7101aae4-1b8c-42bf-ba7b-e2469856888e',
    'Authorization': 'Basic NGRkMThmZjItYTExYi00NjU0LWI1NzYtOTY3YTA4MzI5ZjRhOjJkNWVjYzQ5LWQ1YjctNDNiMy1iMmYwLTdlZTE5YjdlMmU0OQ=='
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    messages = data['messages']
    messages.append({
        'role': 'user',
        'content': prompt
    })
    access_token = json.loads(response.text)['access_token']
    
    url = 'https://gigachat.devices.sberbank.ru/api/v1/chat/completions'
    s = requests.Session()

    headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
    }
    payload ={
        "model": "GigaChat",
        "messages": messages,
        "stream": False,
        "repetition_penalty": 1,
        "function_call": "auto"
    }

    if request.user.is_authenticated:
        if Chat.objects.filter(name=messages[0]['content']):
            pass
        else:
            Chat.objects.create(name=messages[0]['content'], owner=request.user)

        r = s.post(url, headers=headers, data=json.dumps(payload), verify=False)
        return HttpResponse(r.content)
    else:
        r = s.post(url, headers=headers, data=json.dumps(payload), verify=False)
        return HttpResponse(r.content)



def _login(request):
    data = request.POST
    email = data['email']
    password = data['password']
    if User.objects.filter(username=email):
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('error')
    else:
        User.objects.create_user(email, email, password)
        user = authenticate(request, username=email, password=password)
        Setting.objects.create(theme='light_theme', owner=user)
        return HttpResponse('success')