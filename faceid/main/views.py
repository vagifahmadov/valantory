from django.shortcuts import render

# Create your views here.
def home_page(r):
    return render(r, "index.html")

def recognition_page(r):
    return render(r, "recognition.html")