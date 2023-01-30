from django.shortcuts import render, redirect, reverse
from rest_framework.response import Response
from .models import Customer, Region, Food, monthly_plan, Feedback, Orders, Offers
from .serializers import CustomerSerializer, RegionSerializer, FoodSerializer, FeedbackSerializer, OffersSerializer, UserSerializer, AdminPanelSerializer
from rest_framework import serializers
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth.models import User


# User ==============================================================================================================
@api_view(['GET'])
def get_user(request, pk):
    serializer_context = {
            'request': request,
        }
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False,context=serializer_context)

    customer = Customer.objects.get(id=pk)
    serializer2 = CustomerSerializer(customer, many=False,context=serializer_context)
    return Response(serializer2.data)

@api_view(['PUT'])
def edit_user(request, pk):
    objs = User.objects.get(id=pk)
    print(objs.name())
    serializer = UserSerializer(objs, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    data = request.data
    user = User.objects.create( {     
    "user": {
        "email": data["email"],
        "password": data["password"]
    },
    "profile_pic": data["profile_pic"],
    "c_email": data["c_email"],
    "c_phone_number": data["c_phone_number"],
    "address": data["address"],
    "c_region": data["c_region"]
    }
        )
    # objs = User.objects.get(id=pk)
    serializer = UserSerializer(objs, many=False)
    return Response(serializer.data)

# foods=============================================================
@api_view(['GET'])
def get_foods(request):
    serializer_context = {
            'request': request,
        }
    objs = Food.objects.all()
    serializer = FoodSerializer(objs, many=True,context=serializer_context)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_food(request,pk):
    serializer_context = {
            'request': request,
        }
    
    objs = Food.objects.get(id=pk)
    serializer = FoodSerializer(objs, many=False,context=serializer_context)
    return Response(serializer.data)


#admin============================================================================================
@api_view(['POST'])
def add_food(request):
    # objs = Food.objects.all(id=pk)
    data = request.data
    food = Food.objects.create(
            
        f_price = data['f_price'],
        f_name =data['f_name'],
        image_1 = data['image_1'],
        image_2 = data['image_2'],
        image_3 = data['image_3'],
        f_desc = data['f_desc']
        )
    serializer = FoodSerializer(food, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_food(request,pk):
    data = request.data
    food = Food.objects.get(id=pk)

    serializer = FoodSerializer(food, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_food(request,pk):
    food = Food.objects.get(id=pk)
    food.delete()
    return Response('food deleted')

@api_view(['GET'])
def adm_dashboard(request):
    food = Food.objects.all().count()
    orders = Orders.objects.all().count()
    totalsales = Orders.objects.all().filter(status = True).count()
    offers = Offers.objects.all().count()
    customers = Customer.objects.all().count()
    dash = [{
        'food':food,
        'orders':orders,
        'offers': offers,
        'customers': customers,
        'totalsales':totalsales
    }]

    # data = AdminPanelSerializer(Food, Orders, /)

    # return Response(serializer.data)

    return JsonResponse(dash, safe=False)

# on offer============================================================================================
@api_view(['GET'])
def offers(request):
    offer = Offers.objects.all()
    serializer = OffersSerializer(offer, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def offer(request,pk):
    offer = Offers.objects.get(id=pk)
    serializer = OffersSerializer(offer, many=False)

    return Response(serializer.data)




