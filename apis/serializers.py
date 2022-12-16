from rest_framework import serializers
from workout_capstone_app import models

# apis serializer
# creating this nestedexercise ser allows us to acces the exercises within the workout


class NextedExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercise
        fields = [
            'title',
            'description',
            'duration',
            'workout'
        ]


class WorkoutSerializer(serializers.ModelSerializer):
    nested_exercises = NextedExerciseSerializer("nested_exercises", many=True)

    class Meta:
        fields = (
            # base fields for the serializer
            'id',
            'title',
            'description',
            'nested_exercises'
        )
        model = models.Workout


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'description',
            'duration',
            'workout'
        )
        model = models.Exercise

