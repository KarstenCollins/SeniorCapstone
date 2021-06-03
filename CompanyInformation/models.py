from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default="")
    company_name = models.CharField( max_length=100)
    phone_number = models.IntegerField(max_length=10)
    address = models.CharField( max_length=100)
    city = models.CharField( max_length=100)
    state = models.CharField( max_length=2)
    zip = models.CharField( max_length=6)
    website = models.CharField( max_length=100)



    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('view-company')

    #kwargs={'pk': self.pk}
