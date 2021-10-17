from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from .account import Account

class Transaction (models.Model):
    id = models.AutoField(primary_key=True)
    origin_account = models.ForeignKey(Account, related_name='origin',on_delete=CASCADE)
    destiny_account = models.ForeignKey(Account, related_name='destiny',on_delete=CASCADE)
    amount = models.IntegerField(default= 0)
    register_date = models.DateTimeField(auto_now_add=True, blank=True)
    note = models.CharField(max_length=100)

