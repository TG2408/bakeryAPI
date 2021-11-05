from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from . models import IngredientQuantity, Inventory
from . serializers import InventorySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# def stu_detail(request):
#     inve = Inventory.objects.all()
#     serializer = InventorySerializer(inve, many = True)
#     json_data = JSONRenderer().render(serializer.data)

#     a = 2*json_data

#     return HttpResponse(content_type='application/json')


@csrf_exempt
def inventory_list(request):
    if request.method == "GET":
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = InventorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt
def inventory_detail(request, pk):
    try:
        inventory = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = InventorySerializer(inventory)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InventorySerializer(inventory, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        inventory.delete()
        return HttpResponse(status=204)