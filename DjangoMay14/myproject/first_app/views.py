from django.shortcuts import render, redirect
from .models import TestUser,Profile
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    users = TestUser.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'index.html', {'users': users,'profiles':profiles})
def formsub(request):

# Check to see if we get a POST back.
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        uploaded_file = request.FILES.get('document')
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        t = TestUser(first_name=f, last_name=l, email=e, image=uploaded_file)
        t.save()
        return redirect('index')

    else:
        return render(request, 'form.html')