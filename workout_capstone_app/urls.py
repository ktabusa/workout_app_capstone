
from django.urls import path
from . import views

# workout_capstone_app urls.py
urlpatterns = [
    path('', views.index, name='index')
]
