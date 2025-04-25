from django.urls import path
from tkinter.font import names

from .views import home_page, recognition_page, capture_service

urlpatterns = [
    path("", home_page, name="home"),
    path("recognition", recognition_page, name="recognition"),
    path("capture", capture_service, name="capture"),
]