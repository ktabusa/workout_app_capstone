from django.shortcuts import render
from django.http import HttpResponse

# workout_capstone_app views.py


def index(request):
    return HttpResponse('Unused Workout Index')
    # this will be a placeholder page that we won't use for now?


def workout(request, workout_id):
    # passing in the workout_id to the template itself, which makes it usable in the template
    return render(request, 'workout.html', {'workout_id': workout_id})
