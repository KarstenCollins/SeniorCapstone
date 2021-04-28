from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.urls import reverse


#change fields here and then migrate when you put in a real db for Billable
class Post(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, default="")
    account_number = models.CharField(max_length=255, default="")
    statement_date = models.DateField(default=datetime.date.today)
    due_date = models.DateField(default=datetime.date.today)
    date_entered = models.DateField(default=datetime.date.today)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    is_paid = models.BooleanField(default=0)
    payment_method = models.CharField(max_length=50, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE) #this is where the rel. is. Foreign key is the user

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('data-detail', kwargs={'pk': self.pk})