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
    is_paid = models.BooleanField(default=0, help_text="Everything below is optional. Recommended if using a credit card.")
    payment_method = models.CharField(max_length=50, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE) #this is where the rel. is. Foreign key is the user
    previous_balance = models.IntegerField(blank=True, default='0')
    payments = models.IntegerField(blank=True, default='0')
    credit = models.IntegerField(blank=True, default='0')
    adjustment = models.IntegerField(blank=True, default='0')
    late_fees = models.IntegerField(blank=True, default='0')
    interest_charges = models.IntegerField(blank=True, default='0')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('data-detail', kwargs={'pk': self.pk})