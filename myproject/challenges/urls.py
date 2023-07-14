from django.urls import path
from .import views

urlpatterns = [
    #If the request reaches /january, then execute views.index
    #path("january", views.january),
    #place holder syntax for django
    #str: means tells django should be trated as string
    #int: would treat the value as int
    
    #THe third parameter is the label name that the path would be reference with
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
    path("", views.index, name="index")
]
