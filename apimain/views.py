from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from . models import IngredientQuantity, Inventory
from . serializers import InventorySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

# def stu_detail(request):
#     inve = Inventory.objects.all()
#     serializer = InventorySerializer(inve, many = True)
#     json_data = JSONRenderer().render(serializer.data)

#     a = 2*json_data

#     return HttpResponse(content_type='application/json')


#@csrf_exempt
@api_view(['GET','POST'])
def inventory_list(request, format=None):
    if request.method == "GET":
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        #data = JSONParser().parse(request)
        serializer = InventorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def inventory_detail(request, pk, format=None):
    try:
        inventory = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inventory.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)