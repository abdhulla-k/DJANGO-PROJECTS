from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:item_id>/', views.detail, name = 'detail'),
    # add items
    path('add/', views.create_item, name = 'create_item'),
    # edit
    path('update/<int:id>', views.update_item, name= 'update_item')
]