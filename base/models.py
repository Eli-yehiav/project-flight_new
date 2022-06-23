from django.db import models
import datetime

# Create your models here.
class countries(models.Model):
    country_name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.country_name


class UserRoles(models.Model):
    role_name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.role_name

class Users(models.Model):
    username = models.CharField(max_length=50)
    Password = models.IntegerField(default=0)
    email = models.CharField(max_length=50)
    role = models.ForeignKey(UserRoles, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.username




class airline(models.Model):
    country_id= models.ForeignKey(countries, on_delete=models.CASCADE)
    Airline_name = models.CharField(max_length=50)
    User_name = models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.Airline_name

class Customers(models.Model):  
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)  
    address=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    credit_card_number=models.CharField(max_length=50)
    Users_id= models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.first_name

class Flights(models.Model):
    airline_id= models.ForeignKey(airline, on_delete=models.CASCADE)  
    country_origin_id= models.ForeignKey(countries, on_delete=models.CASCADE, related_name='origin')
    destination_id= models.ForeignKey(countries, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    landing_time= models.DateTimeField()
    remaining_tickets=models.IntegerField
    def __str__(self) -> str:
        return f'Flight number' + str(self.id)+'from'+str(self.country_origin_id)+'to'+ str(self.destination_id)

class Tickets(models.Model):
    Flights_id= models.ForeignKey(Flights, on_delete=models.CASCADE)
    Customers_id= models.ForeignKey(Customers, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.Flights_id

class Administor(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)  
    Users_id= models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.first_name


    
      