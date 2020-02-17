# Module that allows us to handle requests
from django.http import HttpResponse
# importing a function to render html templates
from django.shortcuts import render

def home(request):
    return render(request, '../../index.html')
def about(request):
    return HttpResponse("about")
def contact(request):
    return HttpResponse("contact")
def blog(request):
    return HttpResponse("blog")
