from django.shortcuts import render
from .models import User

def all(request):
    users = User.objects.all()
    return render(request , 'firstApp/all.html' , {'users' : users})
