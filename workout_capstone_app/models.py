from django.db import models


# workout_capstone_app models.py


class Workout(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # will need exercises and times? likely need a manytomanyfield for the workouts

    def __str__(self):
        return self.title