from django.contrib import admin
from cal.models import Event

class CalendarDelete(admin.ModelAdmin):
    model = Event
    list_display = ['event']
# Register your models here.
admin.site.register(Event)
