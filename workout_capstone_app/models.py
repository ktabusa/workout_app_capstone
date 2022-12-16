from django.db import models
from django.contrib.auth import get_user_model


# workout_capstone_app models.py


class Workout(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), related_name='owned', on_delete=models.PROTECT, blank=True, null=True)
    # this is trying to link the workout owner to many users... this text does not require a manytomany since we'll have only one owner.

    def __str__(self):
        return self.title


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.FloatField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="nested_exercises")
    # workout = models.ForeignKey will assign it to only a single workout to keep each exercise instance intact 

    def __str__(self):
        return self.title   