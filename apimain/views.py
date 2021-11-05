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
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView


class InventoryList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get(self, request, *args, **kwargs):
        # inventory = Inventory.objects.all()
        # serializer = InventorySerializer(inventory, many=True)
        # return Response(serializer.data)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # serializer = InventorySerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)        

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

# class InventoryDetail(APIView): 
#     def get_object(self, pk):
#         try:
#             return Inventory.objects.get(pk=pk)
#         except Inventory.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         inventory = self.get_object(pk)
#         serializer = InventorySerializer(inventory)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         inventory = self.get_object(pk)
#         serializer = InventorySerializer(inventory, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         inventory = self.get_object(pk)
#         inventory.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# #@csrf_exempt
# @api_view(['GET','POST'])
# def inventory_list(request, format=None):
#     if request.method == "GET":
#         inventory = Inventory.objects.all()
#         serializer = InventorySerializer(inventory, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         #data = JSONParser().parse(request)
#         serializer = InventorySerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# #@csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def inventory_detail(request, pk, format=None):
#     try:
#         inventory = Inventory.objects.get(pk=pk)
#     except Inventory.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = InventorySerializer(inventory)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         #data = JSONParser().parse(request)
#         serializer = InventorySerializer(inventory, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         inventory.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)