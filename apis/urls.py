from django.urls import path
# from .views import ListWorkout, DetailWorkout -- this was removed when we swapped to viewsets
from .views import WorkoutViewSet, ExerciseViewset
from rest_framework.routers import DefaultRouter

# apis app urls.py

# urlpatterns = [
#     path('', ListWorkout.as_view()),
#     path('<int:pk>/', DetailWorkout.as_view()),
# ]


router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workouts')
router.register(r'exercise', ExerciseViewset, basename='exercises')
urlpatterns = router.urls

