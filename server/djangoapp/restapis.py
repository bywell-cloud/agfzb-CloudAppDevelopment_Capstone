import requests
import json
from requests.auth import HTTPBasicAuth
from .models import CarDealer, DealerReview
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

url1="https://edb8d4d7.eu-gb.apigw.appdomain.cloud/api/dealership"


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    #printthe kwargs
    print("GET from {} ".format(url))
    json_data={}
    
    
    try:
       # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        # If  error 
        
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data
    
    
    #try:
     #   if "apikey" in kwargs:
      #      response = requests.get(url, headers={'Content-Type':'application/json'}, params=kwargs, auth=HTTPBasicAuth("apikey", kwargs["apikey"]))
       # else:
        #    response = requests.get(url, headers={'Content-Type':'application/json'}, params=kwargs)

   #     status_code = response.status_code
    #    print("With status {} ".format(status_code))
     #   json_data = json.loads(response.text)
        #print(json_data)
  #  except Exception as e:
     #   print("Error " ,e)
   
    #return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, payload, **kwargs):
    print(url)
    print(payload)
    print(kwargs)
    try:
        response = requests.post(url, params=kwargs, json=payload)
    except Exception as e:
        print("Error" ,e)
    print("Status Code ", {response.status_code})
    data = json.loads(response.text)
    return data

# Create a get_dealers_from_cf method to get dealers from a cloud function
#  get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list

#def get_dealers_from_cf(url1):
 #   results = []
    # Call get_request with a URL parameter
#    json_result = get_request(url1)
    #printthe json_result
 #   if json_result:
        # Get the row list in JSON as dealers
#        dealers = json_result["entries"]
        # For each dealer object
 #       for dealer_doc in dealers:
  #         id=dealer_doc['id']
#            dealer_obj = CarDealer( city=dealer_doc["city"],address=dealer_doc["address"], state=dealer_doc["state"], st=dealer_doc["st"], zip=dealer_doc["zip"],lat=dealer_doc["lat"], long=dealer_doc["long"])
                               
 #           results.append(dealer_obj)

  #  return results

def get_dealers_from_cf(**kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["entries"]
        # For each dealer object
        for dealer_doc in dealers:
            # Get its content in `doc` object
            # dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(dealer_doc)
            results.append(dealer_obj)

    return results




def get_dealers_state(state):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, state=state)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["entries"]
        # For each dealer object
        for dealer_doc in dealers:
            # Get its content in `doc` object
            # dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(dealer_doc)
            results.append(dealer_obj)

    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
def get_dealer_by_id(dealer_id):
    json_result = get_request(url, id=dealer_id)
    if json_result:
        return json_result["entries"]
    else:
        return {'message': 'Something went wrong'}





# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_reviews_from_cf(url, dealer_id):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, dealerId=dealer_id)
    
    if "entries" in json_result:
        reviews = json_result["entries"]
        # For each review object
        for review in reviews:
            review_obj = DealerReview(
                dealership=review["dealership"],
                name=review["name"],
                purchase=review["purchase"],
                review=review["review"],
                purchase_date=review["purchase_date"],
                car_make=review["car_make"],
                car_model=review["car_model"],
                car_year=review["car_year"],
                sentiment=analyze_review_sentiments(review["review"]),
                id=review['id']
                )
            results.append(review_obj)
    #print(results[0])
    return results

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
def analyze_review_sentiments(review, **kwargs):
    apikey="iCbY8nOykgLsdchzXM6GGCQeCsC_VjjY-09Na5Ma9-7I"
    nl_url='https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/f987d097-bf74-426f-a9c4-9dc96d6e4d0f'
    params = json.dumps({"text": review, "features": {"sentiment": {}}})
    response = requests.post(nl-url,data=params,headers={'Content-Type':'application/json'},auth=HTTPBasicAuth("apikey", apikey))
    
    #print(response.json())
    try:
        sentiment=response.json()['sentiment']['document']['label']
        return sentiment
    except:
        return "neutral"
      
      


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



