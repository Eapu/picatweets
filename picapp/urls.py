from django.urls import path
from . import views
app_name = 'picapp'

urlpatterns = [
    path('', views.index, name='index'),

]
