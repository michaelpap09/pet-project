from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class NewUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
