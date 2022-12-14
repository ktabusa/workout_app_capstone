from django.shortcuts import render
from django.http import HttpResponse

# workout_capstone_app views.py


def index(request):
    return HttpResponse('Django Connected')
