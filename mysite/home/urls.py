from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path("",views.index, name="home"),
    path("services",views.services, name="services"),
    path("technologies",views.technologies, name="technologies"),
    path("projects",views.projects, name="projects"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    

]