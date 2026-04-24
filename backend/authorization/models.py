from django.db import models
from django.contrib.auth.models import AbstractUser #28 -> settings.py

# Create your models here.
class CustomUser(AbstractUser): #30 -> adımlar.txt
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.username