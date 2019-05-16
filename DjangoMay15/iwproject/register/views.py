from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'register/index.html')

def form(request):
    return render(request, 'register/form.html')

def registration(request):
    return render(request, 'register/registration.html')