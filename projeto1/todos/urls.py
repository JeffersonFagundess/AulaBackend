from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name='todos'),
    path('index/', views.index, name='index.html'),
]