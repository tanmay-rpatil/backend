from django.contrib.auth.models import AbstractUser
from django.db import models

#user model. Give superuser status to librarian, not so for students
class CustomUser(AbstractUser):
    # can add additional fields
    def __str__(self):
        return (self.username)
