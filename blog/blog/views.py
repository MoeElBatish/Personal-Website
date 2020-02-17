# Module that allows us to handle requests
from django.http import HttpResponse
# importing a function to render html templates
from django.shortcuts import render

def home(request):
    return render(request, 'Templates/index.html')
def about(request):
    return render(request, 'Templates/about.html')
def contact(request):
    return render(request, 'Templates/contact.html')
def blog(request):
    return render(request, 'Templates/blog.html')
