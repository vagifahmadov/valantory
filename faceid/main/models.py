from django.db import models


# Create your models here.
class UserData(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pname = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    id_im = models.IntegerField()
    image = models.CharField(max_length=50)
    base64 = models.CharField(max_length=255)
    folder_url = models.CharField(max_length=20)
