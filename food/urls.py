from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.details, name='details'),
    path('add/', views.addItem, name='addItem'),
    path('update/<int:id>/', views.updateItem, name='update_item'),
    path('delete/<int:id>', views.deleteItem, name='delete_item')
]
