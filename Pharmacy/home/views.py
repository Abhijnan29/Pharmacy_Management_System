from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
   return render(request, 'index.html')
   # return HttpResponse("this is my first page")

def about(request):
    return render(request, 'about.html' )
    #return HttpResponse("This is my about page")

def contact(request): 
        request.method=="post"
        name=request.post.get("name")
        email=request.post.get("email")
        phon=request.post.get("num")
        desc=request.post.get("desc")
        query=contact(name=name,email=email,phoneno=phon,desc=desc)
        query.save()
        messages.info(request,"Thank You. Will Get back you soon {name}")
       
        return render(request, 'contact.html')

def med_prod(request):
    return render(request, 'Med_Prod.html')

def login(request):
    return render(request, 'login.html')

def Register(request):
    return render(request, 'Register.html')

def forget_password(request):
    return render(request, 'forgot_password.html')

def order(request):
    return  render(request, 'order.html')
    return HttpResponse("This is my order page")

def payment(request):
    return render(request, 'payment.html')

def My_cart(request):
    return render(request, 'My_cart.html')


 