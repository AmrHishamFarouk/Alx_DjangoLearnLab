from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model

# Create your models here.
class MyUser(AbstractUser):
    bio = models.TextField(max_length=40,blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True)
    followers = models.ManyToManyField('self',symmetrical=False,related_name='following')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # To avoid naming conflicts
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # To avoid naming conflicts
        blank=True
    )


