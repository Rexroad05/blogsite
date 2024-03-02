from django.shortcuts import render, HttpResponse

#Create views from here
def home(request):
    return HttpResponse("hello world")
