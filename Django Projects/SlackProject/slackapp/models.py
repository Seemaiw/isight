from django.db import models

GENDER_OPTIONS = (
        (1,'Male'),
        (2,'Female'),
    )
# Create your models here.
class TestUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

class Profile(models.Model):
    address = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    gender_option = models.IntegerField(choices=GENDER_OPTIONS)