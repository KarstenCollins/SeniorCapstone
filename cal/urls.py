from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'calendar/', views.CalendarView.as_view(), name='calendar'),
    url(r'event/new/', views.event, name='event_new'),
	url(r'event/edit/(?P<event_id>\d+)/', views.event, name='event_edit'),
    #url(r'event/<int:pk>/remove', views.EventDeleteView.as_view(), name='remove_event'),
    url(r'listcalendar/', views.event_list_view, name='list-calendar'),
    url(r'event/delete/<id>', views.event_delete_view, name='event-delete'),
    url(r'return_home/', views.return_home, name='return_home')
]
