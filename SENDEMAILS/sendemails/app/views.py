from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):

    send_mail('Hey',
    'This is a mail from Django for test meil sending',
    'abdhullak149@gmil.com',
    ['abdhullak96@gmil.com'],
    fail_silently=False)

    return render(request, 'home.html')