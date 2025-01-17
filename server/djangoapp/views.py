
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarMake, CarModel # from .models import related models
from .restapis import get_dealers_from_cf, get_dealer_by_id, get_dealers_state, get_dealer_reviews, post_request   # from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json
import os
import requests
import sys
#from ibmcloudant.cloudant_v1 import CloudantV1
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator , BasicAuthenticator
from urllib.parse import urlencode as original_urlencode
from urllib.parse import uses_params
from django.utils.http import urlencode

#from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

#authenticator = BasicAuthenticator('apikey-v2-16u3crmdpkghhxefd
#from config import CLOUDANT_DB



#auth = BasicAuthenticator("KSJsfNXg4_mYa7TailJYPjAIt4BDHty_egXILz9Vn75M" ,"7a1405f456fc3a0acca4a0ea939068f7")
#service = CloudantV1(authenticator=auth)
#service.set_service_url("https://apikey-v2-15fij93at4ftr36fwwdfuh4po5vcrv58md8rf718308g:7a1405f456fc3a0acca4a0ea939068f7@4ff16b13-4a3a-4608-a787-cbe81ec8dfae-bluemix.cloudantnosqldb.appdomain.cloud")
    

    

# Get an instance of a logger
logger = logging.getLogger(__name__)

url="https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership"
apikey="https://apikey-v2-15fij93at4ftr36fwwdfuh4po5vcrv58md8rf718308g:7a1405f456fc3a0acca4a0ea939068f7@4ff16b13-4a3a-4608-a787-cbe81ec8dfae-bluemix.cloudantnosqldb.appdomain.cloud"
reviewz=''
addreview_url =	"https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/addreview"	
 
review_url = "https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/review"	
 

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
        # Get dealers from the URL

        infoall , info = get_dealers_state(url,state)
        context["infoall"] = infoall
        context["dealerships"] = info
        messages.info(request , "State Not found!!! "  )
        
        # Return a list of dealer short name
        return render(request, 'djangoapp/api_index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    #context = {}
    if request.method == "GET":
        context['title'] = 'Dealership Details'
        context['dealership'] = get_dealer_by_id(dealer_id)
        return render(request, 'djangoapp/dealer_details.html', context)
    
def dealer_details(request, dealer_id):
    context=dict()
    #context = {}
    context['title'] = 'Review Details'
    if request.method == "GET":
        context['dealerid'] = dealer_id
        context['reviews'] = get_dealer_reviews(dealer_id)
        context['msg'] = "Sorry You have to be logged in to add review"
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
            context=dict()
            url="https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership"
        #url = "https://6b6023fb.us-south.apigw.appdomain.cloud/api/dealership"
        
        # Get dealers from the URL

            info  = get_dealers_from_cf(url)
            context["dealerships"] = info
            context["infoall"] = info
            #return HttpResponseRedirect(reverse("index"))
            return render(request, "djangoapp/index.html" ,context)
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
    context=dict()
    url="https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership"
        #url = "https://6b6023fb.us-south.apigw.appdomain.cloud/api/dealership"
        
        # Get dealers from the URL

    info  = get_dealers_from_cf(url)
    context["dealerships"] = info
    context["infoall"] = info
    
    #return HttpResponseRedirect(reverse("index"))
    return render(request, "djangoapp/index.html" , context)
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
    
    if request.method == "GET":
        context=dict()
        url="https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership"
        #url = "https://6b6023fb.us-south.apigw.appdomain.cloud/api/dealership"
        
        # Get dealers from the URL

        info  = get_dealers_from_cf(url)
        context["dealerships"] = info
        context["infoall"] = info
        
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
    addreview_url =	"https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/addreview"
    if request.method == "GET":
        
        context=dict()
        context['dealer_id'] = dealer_id
        context['username'] = request.user.username 
        context['cars'] = CarModel.objects.all()

        return render(request, 'djangoapp/add_review.html', context)
    if request.method == "POST":
        car_id = request.POST.get('car')
        car = CarModel.objects.get(id=car_id)
        carname=car.name
        caryear=str(car.year)
        carmake = car.carmake
        di = dealer_id
        cn = request.POST.get('content')
        usn = request.POST.get('username')
        pd = str(request.POST.get('purchase_date'))

        purchase = request.POST.get('purchase_check')
        if purchase == 'on':
            p = 'True'
        else:
            p = 'False'
        cmo = car.car_type

        return redirect('https://079110cb.eu-gb.apigw.appdomain.cloud/eg/eg'+'?'+urlencode({'cnm':carname})+'&'+urlencode({'cy':caryear})+'&'+urlencode({'cm':carmake})+'&'+urlencode({'di':di})+'&'+urlencode({'cn':cn})+'&'+urlencode({'usn':usn})+'&'+urlencode({'pd':pd})+'&'+urlencode({'p':p})+'&'+urlencode({'cmo':cmo})) 


        #-review = {} 
        #review['time'] = datetime.utcnow().isoformat().split('T')[0]
        #-review['dealership'] = dealer_id

    
        #-review['review'] = request.POST.get('content')
        #-review['name'] = request.POST.get('username')
        #-review['purchase_date'] = str(request.POST.get('purchase_date'))
        #-review['car_model'] = car.name
        #-review['car_year'] = str(car.year)
        #review['car_make'] = car.carmake

    #-    if purchase == 'on':
      #-      review['purchase'] = 'True'
        #-else:
          #-  review['purchase'] = 'False'

   #-     if request.user and request.user.is_authenticated:
     #-       json_payload = { "review": review }
      #  products_doc = {
       # "car_make": "Bmw","car_model": "suden",
        #"car_year": 2000,"dealership": 13,
      #  "id":210,"name": "Richardy","purchase": 'true',
       # "purchase_date": "09/17/2020","review": "testing12"
      #  }    
        
        pass
        
        
        #-response = service.post_document(db='reviews', document=json_payload).get_result()
        #-if response:
        #response = service.post_all_docs(db='reviews', include_docs=True).get_result()
          #-  response = service.post_find(db='reviews',selector={"dealership": {'$eq':int(dealer_id)}},fields=['id','name','dealership','review','purchase','purchase_date','car_make','car_model','car_year']).get_result()
           #- return redirect("djangoapp:dealer_details" ,{"data":response ,"dealer_id":dealer_id })
        #-else:
            
          #-  return redirect("djangoapp:dealer_details" ,{"data":response ,"dealer_id":dealer_id , "error":"Sorry Someting when wrong , Not saved" })
     
