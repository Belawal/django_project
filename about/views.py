from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_me(request):
    return HttpResponse("Thus wirkd be the about page instead")
