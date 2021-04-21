from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bank_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True)
    account_type = models.CharField(max_length=255)
    bank_acc_number = models.IntegerField()
    routing_number = models.IntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.bank_name
    
    def get_absolute_url(self):
        return reverse('view-banks')
        #kwargs={'pk': self.pk}