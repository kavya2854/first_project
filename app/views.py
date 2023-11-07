from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def django(request):
    return HttpResponse('<h1><marquee>Hi How are you?</h1></marquee>')

def jamPandu(request):
    return HttpResponse('<h1 style="background-color:red; width:400px height:200px">What are u dng?Had Breakfast</h1>')
    
