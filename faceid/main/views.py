from importlib.metadata import requires
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json


# Create your views here.
def home_page(r):
    return render(r, "index.html")


def recognition_page(r):
    # print(list(r))
    # request_type = str(str(list(r)[0]).split("&")[1]).split('=')[1].replace("'", "")
    # print(f'\n\n\n\n===================\n{request_type}\n---------------------\n\n\n\n')
    return render(r, "recognition.html")


@csrf_exempt
def capture_service(r):
    if r.method == 'POST':
        print('POSTed')
        data = json.loads(r.body)
        b64_img = data.get('b64img')
        ip_addr = data.get('ip')
        print(f'\n\n\n\n===================\n{data}\n---------------------\n\n\n\n')
        return JsonResponse({'received': True, 'key1': b64_img, 'key2': ip_addr})
    else:
        return None


@csrf_exempt
def pin_service(r):
    if r.method == 'POST':
        print('pin posted\n')
        data = json.loads(r.body)
        b64_img = data.get('b64img')
        pin = data.get('pin')
        return JsonResponse({'received': True, 'key1': b64_img, 'key2': pin})
    else:
        return None
