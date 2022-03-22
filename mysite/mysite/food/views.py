import imp
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'food/index.html')
