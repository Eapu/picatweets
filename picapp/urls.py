from django.urls import path
from . import views
app_name = 'picapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('pic', views.index2, name='index2'),


]
