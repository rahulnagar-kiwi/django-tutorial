from django.urls import path
from . import views
urlpatterns = [path('nagar/1', views.index, name='index'),
               ]
