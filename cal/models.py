from django.db import models
from django.urls import reverse, reverse_lazy

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cal:event-edit', args=(self.id,))
        #return reverse_lazy('cal:remove_event', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        #url = reverse_lazy('cal:remove_event', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class EventMemberDelete(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event']

    def __str__(self):
        return str(self.user)
