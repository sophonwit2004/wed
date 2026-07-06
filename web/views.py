from django.shortcuts import render, HttpResponse, get_object_or_404, redirect


# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")
    