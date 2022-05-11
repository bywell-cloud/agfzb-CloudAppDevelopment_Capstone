from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + "," + \
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
class CarDealer1:
    def __init__(self, dealership):
        for key,value in dealership.items():
            setattr(self, key, value)

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview1:
    def __init__(self, review, sentiment):
        for key,value in review.items():
            setattr(self, key, value)
        self.sentiment = sentiment

    def __str__(self):
        return "Dealer name: " + self.full_name

class CarDealer:
    def __init__(self, address, city, full_name, id, 
                    lat, long, short_name, st, state, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.state = state
        self.zip = zip

    def __str__(self):
        return self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
# Sentiment will be reviewed 


class DealerReview():
    def __init__(self, id, name, review, purchase, car_make, car_model, car_year, purchase_date):
        self.id = id
        self.name = name
        self.review = review
        self.purchase = purchase
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.purchase_date = purchase_date

    def __str__(self):
        return self.name
