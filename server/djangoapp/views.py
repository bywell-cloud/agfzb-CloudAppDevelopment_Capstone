from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context = {}
    return render(request, 'djangoapp/about.html', context)
# ...


# Create a `contact` view to return a static contact page 
def contact(request):
    context = {}
    return render(request, 'djangoapp/contact.html', context)


#api_all
def dealerships(request):
    
    req0 =requests.get('https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership')
   
    req= req0.json()
    context = {'req':req}
    print(req)
    #return render(request,'apiapp/index.html',{'req':req})
    return render(request, 'djangoapp/api_index.html', context)
 
#api_sngle
def dealerships_s(request,state):
    
    req0 =requests.get('https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership')
    
    state=state
    req= req0.json()
    context = {'req':req,'state':state}
    print(req)
    #return render(request,'apiapp/index.html',{'req':req})
    return render(request, 'djangoapp/api_index_s.html', context)







# Create a `login_request` view to handle sign in request
def login_request(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            #return HttpResponseRedirect(reverse("index"))
            return render(request, "djangoapp/index.html")
        else:
            return render(request, "djangoapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "djangoapp/login.html")
# ...


# Create a `logout_request` view to handle sign out request
def logout_request(request):

    logout(request)
    #return HttpResponseRedirect(reverse("index"))
    return render(request, "djangoapp/index.html")
# ...

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "djangoapp/registration.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except:
            return render(request, "djangoapp/registration.html", {
                "message": "Username already taken."
            })
        login(request, user)
        #return HttpResponseRedirect(reverse("index"))
        return render(request, "djangoapp/index.html")
    else:
        return render(request, "djangoapp/registration.html") 
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

