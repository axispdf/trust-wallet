from asyncio.windows_events import NULL
from email.policy import default
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.conf import settings
from django.db import models
from django.db import models


User = settings.AUTH_USER_MODEL



class Bio(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.CharField()

    def __str__(self):
        return  f'Id {self.users}: {self.balance}'