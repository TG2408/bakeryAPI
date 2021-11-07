from django.contrib.auth import login

from . models import IngredientQuantity, Inventory, Products
from . serializers import InventorySerializer, UserSerializer, RegisterSerializer, IngredientQuantitySerialzer, ProductsSerializer, AvialableProductSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, mixins, generics, generics, permissions, serializers
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from knox.models import AuthToken


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#Login API
class LoginAPI(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

#Inventory API   
class InventoryList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]  
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]  
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

#Products API
class ProductList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]  
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]  
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

#Ingredient Quantiity API
class IngredientQuantityList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]  
    queryset = IngredientQuantity.objects.all()
    serializer_class = IngredientQuantitySerialzer

class IngredientQuantityDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]  
    queryset = IngredientQuantity.objects.all()
    serializer_class = IngredientQuantitySerialzer


@api_view(['GET','POST'])
def available_products(request, format=None):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  
    if request.method == "GET":
        products = Products.objects.all()
        serializer = AvialableProductSerializer(products, many=True)
        return Response(serializer.data)

# #
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

# class InventoryDetail(APIView): 
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
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

# class InventoryList(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView,
#                     APIView):

#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAdminUser]   

#     queryset = Inventory.objects.all()
#     serializer_class = InventorySerializer

#     def get(self, request, *args, **kwargs):
#         # inventory = Inventory.objects.all()
#         # serializer = InventorySerializer(inventory, many=True)
#         # return Response(serializer.data)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         # serializer = InventorySerializer(data = request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return self.create(request, *args, **kwargs)     



# # class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Inventory.objects.all()
# #     serializer_class = InventorySerializer

# class InventoryDetail(APIView): 
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
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