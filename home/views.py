from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # print(request.META)
    return HttpResponse('Hello, Django!')
    
def dinner(request):
    box = ['치킨', '치킨', '롯데리아']
    dinner = random.choice(box)
    return HttpResponse(dinner)