from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

#main user
class User(AbstractUser):
    
    def __str__(self):
        return self.username



