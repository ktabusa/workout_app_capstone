from django.shortcuts import render

# apis app views.py

from rest_framework import generics, viewsets

from workout_capstone_app import models
from .serializers import WorkoutSerializer, ExerciseSerializer


# class ListWorkout(generics.ListCreateAPIView):
#     queryset = models.Workout.objects.all()
#     serializer_class = WorkoutSerializer


# class DetailWorkout(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Workout.objects.all()
#     serializer_class = WorkoutSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = models.Workout.objects.all()
    serializer_class = WorkoutSerializer


class ExerciseViewset(viewsets.ModelViewSet):
    queryset = models.Exercise.objects.all()
    serializer_class = ExerciseSerializer
