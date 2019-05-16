from django.shortcuts import render, redirect
from .models import userform
from django.contrib.auth.models import User
from .models import userform
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'register/index.html')

def register(request):
    return render(request, 'register/registration.html')

def list(request):
    members = userform.objects.all()
    return render(request, 'register/iwform.html', {'members': members})

def submit(request):
    if request.method =='POST':
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=uname,email=email, password=password)
        user.save()
        return redirect('index')
    else:
        return render(request, 'register/registration.html')
def iwform(request):
    if request.method == 'POST':
        name = request.POST['full_name']
        e = request.POST['email']
        phone = request.POST['phone']
        upload_cv = request.FILES.get('file')
        upload_photo = request.FILES.get('file1')
        check = request.POST.get('check', False)
        check1 = request.POST.get('check1', False)
        check2 = request.POST.get('check2', False)
        textarea = request.POST['textarea']
        fs = FileSystemStorage()
        fs.save(upload_cv.name, upload_cv)
        fs.save(upload_photo.name, upload_photo)
        member = userform(full_name=name, email=e, phone_number=phone, cv = upload_cv, image = upload_photo,radio =check,radio1 =check1,radio2 = check2, text = textarea)
        member.save()
        return redirect('list')
    else:
        return render(request, 'register/index.html')
