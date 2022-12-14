from rest_framework import serializers
from workout_capstone_app import models

# apis serializer


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            # base fields for the serializer
            'id',
            'title',
            'description',
        )
        model = models.Workout
