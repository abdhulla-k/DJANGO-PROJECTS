import imp
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.

def index(request):
    data = Item.objects.all()
    context = {
        'data':data
    }
    return render(request, 'food/index.html',context)

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(request,'food/detail.html',context)