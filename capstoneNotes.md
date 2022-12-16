custom user models
use api to save workouts
page to create workouts
get requests to load
page to run an existing workout with timers


12/13/22
Created custom user model 

12/14/22
created apis app and links with the DRF learndjango tutorial but swapped it to workouts
https://learndjango.com/tutorials/django-rest-framework-tutorial-todo-api

Added workout class, and an exercise class,
workouts can have an 'owner' where they can use other (ie. admin's workouts) but not edit the times/exercises.

Could have a copy feature to create a user version of an 'admin' workout to edit and save
user can only edit their own workout instances so the base workout data isn't changed each time


For creating viewsets: Need to have a serializer, then we update the api views.py with the viewset, and then we update the api urls with the urlpatters.


ACTION - need to add a workout detail page / workout start page


Optional adds 
- needs to add owner functionality
- Can add workout classes for rest/work to have a different display?
