from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default="")
    source_name = models.CharField( max_length=100)
    amount = models.CharField( max_length=20)
    date_received = models.CharField( max_length=12)

    def __str__(self):
        return self.source_name
    
    def get_absolute_url(self):
        return reverse('view-Income', kwargs={'pk': self.pk})

