from django.urls import path
from knox import views as knox_views
from rest_framework import views
from .views import  RegisterAPI, LoginAPI, InventoryList, InventoryDetail, ProductList, ProductDetail, IngredientQuantityList, IngredientQuantityDetail
from . import views

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('inventory/', InventoryList.as_view()),
    path('inventory/<int:pk>/', InventoryDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('ingredientQuantity/', IngredientQuantityList.as_view()),
    path('ingredientQuantity/<int:pk>/', IngredientQuantityDetail.as_view()),
    path('available_products/',views.available_products),
    path('orders/<str:name>/', views.orders),
]