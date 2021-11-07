from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt

from . models import IngredientQuantity, Inventory, Orders, Products
from . serializers import OrdersSerializer, InventorySerializer, UserSerializer, RegisterSerializer, IngredientQuantitySerialzer, ProductsSerializer, AvialableProductSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, mixins, generics, generics, permissions, serializers
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication

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

# Avialable products API
@api_view(['GET','POST'])
def available_products(request, format=None):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  
    if request.method == "GET":
        products = Products.objects.all()
        serializer = AvialableProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def orders(request, name, format=None):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]  
    if request.method == "GET":
        orders = Orders.objects.filter(user = name)
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)

@csrf_exempt
def new_order(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrdersSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






        
