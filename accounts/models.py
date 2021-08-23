from django.contrib.auth.models import AbstractUser
from django.db import models

#user model
def error_dict():
	return {'error':''}

class CustomUser(AbstractUser):
    # can add additional fields
    properties  = models.JSONField(blank=False, null=False, default=error_dict())
    def __str__(self):
        return (self.username)
