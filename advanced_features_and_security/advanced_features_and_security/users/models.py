from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)  # Add date_of_birth field
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Add profile_photo field
