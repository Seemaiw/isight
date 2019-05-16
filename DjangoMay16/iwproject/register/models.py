from django.db import models

class userform(models.Model):
    full_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=15)
    phone_number = models.CharField(max_length=20)
    cv = models.FileField(blank=True, upload_to="cv")
    image = models.FileField(blank=True, upload_to="profile_pics")
    radio = models.CharField(max_length=15)
    radio1 = models.CharField(max_length=15)
    radio2 = models.CharField(max_length=15)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
