from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        # an other method for get data from form is below
        firstName = request.POST['fname']
        secondName = request.POST['lname']
        emailId = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username, emailId, password1)
        myuser.firstName = firstName
        myuser.secondName = secondName

        myuser.save()

        messages.success(request, 'Your has been successfully created')

        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signout(request):
    pass