from django.conf import settings
from django.db import models
import datetime

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

User = settings.AUTH_USER_MODEL



class Bio(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        return  f'Id {self.users}: {self.balance}'



class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adress = models.CharField(max_length=100)
    amount = models.CharField(max_length=30)
    crypto = models.CharField(max_length=30)
    datatimes = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'ЮЗЕР: {self.user}: ЦЕНА {self.amount}: КРИПТА {self.crypto}'