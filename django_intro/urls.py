"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path 
from django.urls import path, include
# from home import views
# from utilities import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.site.urls')),
    # 요청이 home/으로 오면, home/urls.py으 ㅣ설정들에 맞춰 뷰로 보내준다.
    # path('home/', include('home.urls')),
#     path('home/', views.index),
#     path('home/dinner/', views.dinner),
#     path('home/you/<name>/', views.you),
#     path('home/cube/<int:num>/', views.cube),
#     path('home/ping/', views.ping),
#     path('home/pong/', views.pong),
#     path('home/user_new/', views.user_new),
#     path('home/user_read/', views.user_read),
#     path('home/template_example/', views.template_example),
#     path('home/static_example/', views.static_example),
]
