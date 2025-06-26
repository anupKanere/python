
from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.all , name="firstApp_home"), # localhost:8000/firstApp

]
