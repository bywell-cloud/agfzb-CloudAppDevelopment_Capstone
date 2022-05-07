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
    def __init__(self, dealership):
        for key,value in dealership.items():
            setattr(self, key, value)

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, review, sentiment):
        for key,value in review.items():
            setattr(self, key, value)
        self.sentiment = sentiment

    def __str__(self):
        return "Dealer name: " + self.full_name


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
