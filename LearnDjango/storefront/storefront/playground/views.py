from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def SayHello(request):
   # return HttpResponse('Hello world')
   data = Item.objects.all()
   return HttpResponse(request,data)