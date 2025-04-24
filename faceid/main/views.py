from django.shortcuts import render
import json

# Create your views here.
def home_page(r):
    return render(r, "index.html")

def recognition_page(r):
    request_type = str(str(list(r)[0]).split("&")[1]).split('=')[1].replace("'", "")
    print(f'\n\n\n\n===================\n{request_type}\n---------------------\n\n\n\n')
    return render(r, "recognition.html")