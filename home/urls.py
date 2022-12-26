from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.input,name='home'),
    path('scraper',views.scraper, name='scraper')
]