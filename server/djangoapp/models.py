from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + "-" + \
               "Description: " + self.description

class CarModel(models.Model):
    name = models.CharField(null=False, max_length=30)
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    OTHER = 'other'
    CAR_TYPE_CHOICES = [
        (BENZ = 'Benz'),
        (BMW , 'Bmw'),
        (SEDAN, 'Sedan'),
        (SUV, 'SuV'),
        (WAGON, 'Wagon'),      
        (OTHER, 'Other')
        
    ]
    car_type = models.CharField(
        max_length=10,
        choices=CAR_TYPE_CHOICES,
        default=OTHER,
    )
    year = models.DateField()

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Type: " + self.car_type + "," + \
               "Year: " + self.year.strftime("%Y")
    
# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, id, full_name, short_name, city, address, state, st, zip, lat, long):
        self.id = id
        self.full_name = full_name
        self.short_name = short_name
        self.city = city
        self.address = address
        self.state = state
        self.st = st
        self.zip = zip
        self.lat = lat
        self.long = long

    def __str__(self):
        return 'Dealer Name: ' + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, id, car_make, car_model, car_year, dealership, name, purchase, purchase_date, review, sentiment):
         self.id = id
         self.car_make = car_make
         self.car_model = car_model
         self.car_year = car_year
         self.dealership = dealership
         self.name = name
         self.purchase = purchase
         self.purchase_date = purchase_date
         self.review = review
         self.sentiment = sentiment

    def __str__(self):
        return 'Review name ' + self.name    


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
#class CarDealerZZ:
   # def __init__(self, dealership):
 ##       for key,value in dealership.items():
    #        setattr(self, key, value)

    #def __str__(self):
     #   return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
#class DealerReviewZZ:
 #   def __init__(self, review, sentiment):
  #      for key,value in review.items():
   #         setattr(self, key, value)
    #    self.sentiment = sentiment

    #def __str__(self):
     #   return "Dealer name: " + self.full_name


