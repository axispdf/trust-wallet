from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL



class Bio(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length=30)

    def __str__(self):
        return  f'Id {self.users}: {self.balance}'



class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    amount = models.CharField(max_length=30)
    crypto = models.CharField(max_length=30)
    datatimes = models.DateTimeField()

    def __str__(self):

        return  f'ЮЗЕР: {self.user}: ЦЕНА {self.amount}: КРИПТА {self.crypto}'