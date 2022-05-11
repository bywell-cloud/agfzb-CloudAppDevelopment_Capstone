
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarMake, CarModel # from .models import related models
from .restapis import get_dealers_from_cf, get_dealer_by_id, get_dealers_state, get_dealer_reviews_from_cf, post_request   # from .restapis import related methods
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

url="https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership"
apikey="https://apikey-v2-15fij93at4ftr36fwwdfuh4po5vcrv58md8rf718308g:7a1405f456fc3a0acca4a0ea939068f7@4ff16b13-4a3a-4608-a787-cbe81ec8dfae-bluemix.cloudantnosqldb.appdomain.cloud"
reviewz='https://2e35c4b8.eu-gb.apigw.appdomain.cloud/api/review'

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
def dealerships2(request):
    
    req0 =requests.get('https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership')
   
    req= req0.json()
    context = {'req':req}
    print(req)
 #   return render(request,'apiapp/index.html',{'req':req})
    return render(request, 'djangoapp/api_index.html', context)
 
#api_sngle

  
def get_dealer_state(request, state):
    context = {}
    context['title'] = 'Dealership State'
    if request.method == "GET":
        state0=get_dealer_state(state)
        jsn=state0.json()
        print(jsn)
        context={'state':jsn}
        # context['reviews'] = get_dealer_reviews_from_cf(dealer_id)
               
        return render(request, 'djangoapp/dealer_state.html', context)
    





def dealerships_s(request,state):
    
    req0 =requests.get('https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership')
    
    state=state
    req= req0.json()
    context = {'req':req,'state1':state}
    print(req)
    #return render(request,'apiapp/index.html',{'req':req})
    return render(request, 'djangoapp/api_index_s.html', context)

def dealerships(request):

    if request.method == "GET":
        context=dict()
        url="https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership"
        #url = "https://6b6023fb.us-south.apigw.appdomain.cloud/api/dealership"
        
        # Get dealers from the URL

        info  = get_dealers_from_cf(url)
        context["dealerships"] = info
        context["infoall"] = info
        #context["result"] = result
        #context["infoall"] = infoall
        
        # Return a list of dealer short name
        return render(request, 'djangoapp/api_index.html', context)



def dealerships3(request):

    if request.method == "POST":
        state = request.POST["state"]

        context=dict()
        url="https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership"
        #url = "https://6b6023fb.us-south.apigw.appdomain.cloud/api/dealership"
        
        # Get dealers from the URL

        infoall , info = get_dealers_state(url,state)
        context["infoall"] = infoall
        context["dealerships"] = info
        messages.info(request , "State Not found!!! "  )
        
        # Return a list of dealer short name
        return render(request, 'djangoapp/api_index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    context = {}
    context['title'] = 'Dealership Details'
    if request.method == "GET":
        context['dealership'] = get_dealer_by_id(dealer_id)
        return render(request, 'djangoapp/dealer_details.html', context)
    
def get_dealer_reviewdetails(request, dealer_id):
    context = {}
    context['title'] = 'Review Details'
    if request.method == "GET":
        context['reviews'] = get_dealer_reviews_from_cf(dealer_id)
        return render(request, 'djangoapp/dealer_reviewdetails.html', context)    
  


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





# Update the `get_dealerships` view to render the index page with a list of dealerships

# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    if request.method == "GET":
        context = {}
        context['dealer_id'] = dealer_id
        context['username'] = request.user.first_name + " " + request.user.last_name
        context['cars'] = CarModel.objects.all()

        return render(request, 'djangoapp/add_review.html', context)
    if request.method == "POST":
        car_id = request.POST.get('car')
        car = CarModel.objects.get(id=car_id)
        purchase = request.POST.get('purchase')

        review = {}
        review['time'] = datetime.utcnow().isoformat().split('T')[0]
        review['dealership'] = dealer_id
        review['review'] = request.POST.get('review')
        review['name'] = request.POST.get('username')
        review['purchase_date'] = request.POST.get('purchasedate')
        review['car_model'] = car.name
        review['car_year'] = car.year.year
        review['car_make'] = car.carmake.name

        if purchase == 'on':
            review['purchase'] = True
        else:
            review['purchase'] = False

        if request.user and request.user.is_authenticated:
            json_payload = { "review": review }
            post_request(reviewz, json_payload, dealerId=dealer_id)
            return redirect("djangoapp:dealer_details", dealer_id)
        else:
            return redirect("djangoapp:dealer_details", dealer_id)

