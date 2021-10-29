from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile = models.ImageField(default='user_default_m.png', upload_to='profile/', blank=True, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)

    # def __str__(self):
    #     return self.first_name