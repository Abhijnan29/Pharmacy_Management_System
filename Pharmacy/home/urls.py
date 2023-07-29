from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact", views.contact),
    path("login/",views.login),
    path("Register/",views.Register),
    path("forget_password/",views.forget_password),
    path("med_prod/",views.med_prod),
    path("order/", views.order),
    path("payment/",views.payment),
    path("My_cart/",views.My_cart),

]