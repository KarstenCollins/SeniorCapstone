from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from djmoney.models.fields import MoneyField
import datetime

# Create your models here.

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default="")
    source_name = models.CharField( max_length=100)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    date_received = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.source_name
    
    def get_absolute_url(self):
        return reverse('view-Income')
    
    #kwargs={'pk': self.pk}

