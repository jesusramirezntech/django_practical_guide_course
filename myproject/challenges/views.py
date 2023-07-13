from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#renders the html template as text so it can be sent as http response
from django.template.loader import render_to_string

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
        challenge_text = monthly_challenges[month]
        #response_data = f"<h1>{challenge_text}</h1>"
        #return HttpResponse(render_to_string("challenges/challenge.html"))
        #THe following is the same as the two lines above
        return render(request, "challenges/challenge.html",{
            "text" : challenge_text
        })
    except:
        return HttpResponseNotFound("This path is not supported")

def index(request):
    list_items = ""
    months = monthly_challenges.keys()
    
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"
        
        
    html_list = f"<ul>{list_items}</ul>"
    
    return render(request,"challenges/index.html", {
        "months" : months
    })
