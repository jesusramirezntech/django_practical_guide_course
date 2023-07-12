from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january" : "This is january",
    "february" : "This is february",
    "march" : "This is march",
    "april" : "This is april",
    "may" : "This is may",
    "june" : "This is june",
    "july" : "This is july",
    "august" : "This is august",
    "september" : "This is september",
    "october" : "This is october",
    "november" : "This is november",
    "december" : "This is december",
}
# Create your views here.
"""
def monthly_redirect(request,month):
    return HttpResponseRedirect("/challenges/" + somePath)
"""


#Using labeled URLs
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month index")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

#month SHOULD BE the same name defined in the URLs file path
def monthly_challenge(request, month):
    
    try:
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("This path is not supported")

