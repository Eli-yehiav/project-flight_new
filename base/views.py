from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Users, airline
from rest_framework.decorators import api_view


# Create your views here.
def index(r):
    return HttpResponse('test')

@api_view(['GET','POST'])
def users(r):
    if r.method=='GET':
        users=Users.objects.all().values()
        print (users)
        return JsonResponse(list(users), safe=False)
    if r.method=='Post':   #create
        user= r.data('username')
        temp = Users.objects.filter(username= user).values()
        return JsonResponse(temp)

  

    
        