from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    self_description = models.TextField(blank=True)


