from django.contrib import admin

from base.models import Administor, Customers, Flights, Tickets, UserRoles, Users, airline, countries

# Register your models here.
admin.site.register(countries)
admin.site.register(Flights)
admin.site.register(Customers)
admin.site.register(Users)
admin.site.register(UserRoles)
admin.site.register(airline)
admin.site.register(Administor)
admin.site.register(Tickets)
