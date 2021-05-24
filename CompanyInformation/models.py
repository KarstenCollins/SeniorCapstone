from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=10, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=6)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('view-companys')
        #kwargs={'pk': self.pk}
