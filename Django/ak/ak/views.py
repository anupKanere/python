from django.http import HttpResponse
from django.shortcuts import render

def health_check(request):
    # return HttpResponse("Health check ...Server Running successfully")
    return render(request , 'index.html')


def about(request):
    return HttpResponse("Welcome to Django Series")

def contact(request):
    return HttpResponse("visit www.abc.com for more info")

