from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#change fields here and then migrate when you put in a real db for Billable
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #this is where the rel. is. Foreign key is the user
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('data-detail', kwargs={'pk': self.pk})