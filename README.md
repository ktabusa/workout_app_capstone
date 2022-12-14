<!-- Here is My Capstone Proposal -->

# Workout Timer App


## Project Overview
This project is intended to help a people wtime and visualize their workouts without having to look down at list of exercises or manually time each step of their completion.

Libraries/Frameworks: Python, Vue, Django Rest Framework (Serializers). Maybe a visualization library for nice to have features.


## Features
The ability to have default and pre-saved workouts populated without logging in or prior to creating a profile.

User generated workouts can be saved and made available at subsequent logins.

Additional features to track last workout completion, all dates complete, and number of times a workout has been completed. Can also have a list of the last weights used for a workout. 


### User Stories
<!-- Ask about additional user stories or if I can break some of these to be more specific.  IE I kept having to mentally track times for a workout leads to timer fxn.  Thinking of and referring to an exercise list is the exercise name / list fxn.  -->

**As a new app user I want to have a few base workouts available by default upon opening the app so I can launch the app and just start a beginner or basic workout.**
**Tasks:**
- Create basic workouts to start usage immediately
- Have the button based functionality to click a start button to begin a workout
- Workout interface to count down time left in the workout and each set remaining.
- Allow the user to workout without logging in


**The user needs to be able to save their own personalized workouts**
**Tasks:**
- Need to be able to have login functionality and to be able to save user workout data
- A separate page or additional funtionality built in to the base workout page to type in exercise titles, enter a time or rep count, and then input set and round numbers for the workout.


**The user wants to see workout data for their app usage**
**Tasks:**
- Include functionality to track number of times a workout was completed, dates completed, date last completed. 




## Data Model
<!-- Custom user model functionality needs to be included at the beginning! -->
**User**
- Workouts

**Workouts**
- Exercises
- Set time / Reps
- Completion counter
- Date last completed
- Dates completed
- Weights used


## Schedule
**Week 1**
- Create a custom user model just in case I want to include additional functionality (MVP)
- Complete workout page (MVP)
- Workout page needs to be able to have a timer to count down the workout time duration, set time duration, and sets/rounds remaining

**Week 2**
- Create User login functionality(MVP)
- Create functionality for users to create and save workouts(MVP)
- Dial in clean UI feel for the pages above 

**Week 3**
- Update workouts with rep functionality so that all sets or rounds aren't time duration based.
- Continue polishing UI with bar chart / pie chart like visualization to show the time remaining visually

**Week 4**
- Include functionality to track workout date/time completion (nice to have)
- Integrate components to track a number of times a workout has been completed(nice to have)
- Add in functionality to track workout weights (nice to have)
