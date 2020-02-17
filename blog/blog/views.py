# Module that allows us to handle requests
from django.http import HttpResponse
# importing a function to render html templates
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog.html')
