from django.urls import path
from . import views
    #period is current dir

urlpatterns = [
    path('', views.home, name='Submit-Data'),
        #'' means home
    path('about/', views.about, name='About-Submit-Data')
]       

