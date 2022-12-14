from django.db import models
from django.contrib.auth.models import AbstractUser

# accounts models.py


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
