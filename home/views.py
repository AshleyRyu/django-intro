from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # print(request.META)
    return HttpResponse('Hello, Django!')