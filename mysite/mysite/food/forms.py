from pyexpat import model
from urllib import request
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_disc', 'item_price', 'item_image']