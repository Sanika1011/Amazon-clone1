from django.contrib import admin
from django.urls import path
from . import views

# urlpatterns = [
#     path('',views.index,name='index'),
#     path('seemore',views.seemore,name='seemore'),
#     # path('add',views.add,name='add'),
#     path('add/', views.add, name='add'),
# ]


urlpatterns = [
    path('', views.index, name='index'),
    path('seemore/', views.seemore, name='seemore'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]    
