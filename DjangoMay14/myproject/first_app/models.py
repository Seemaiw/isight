from django.db import models


class TestUser(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.FileField(blank=True, upload_to="userimages")

    def __str__(self):
        return self.first_name

class Profile(models.Model):
    address = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=20)

    testuser = models.OneToOneField(TestUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.address