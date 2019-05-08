from django.contrib import admin

# Register your models here.
from .models import TestUser
from .models import Profile


admin.site.register(TestUser)
admin.site.register(Profile)