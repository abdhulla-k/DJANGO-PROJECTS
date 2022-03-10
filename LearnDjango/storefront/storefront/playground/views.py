from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def SayHello(request):
   # return HttpResponse('Hello world')
   return render(request , 'hello.html', {'name':'Abdhu'})