from django.shortcuts import render
from django.shortcuts import HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

def index(request):
    #return HttpResponse("this is Home page...")
    
    return render(request,"index.html")

def services(request):
    return HttpResponse("this is Sevices page...")

def technologies(request):
    return HttpResponse("this is Technology page...")

def projects(request):
    return HttpResponse("this is project page...")

def about(request):
    return HttpResponse("this is About page...")

def contact(request):
   # return HttpResponse("this is   contact page...")
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        
        contact=Contact()
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.desc=desc
        contact.date=datetime.today()
        contact.save()

        print(contact)

        messages.success(request, 'Your Message has been sent!')


    return render(request,"contact.html")
