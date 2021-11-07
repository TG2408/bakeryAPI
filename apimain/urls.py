from django.urls import path
from knox import views as knox_views
from .views import RegisterAPI, LoginAPI, InventoryList, InventoryDetail

urlpatterns = [
    path('buyer/register/', RegisterAPI.as_view(), name='register'),
    path('buyer/login/', LoginAPI.as_view(), name='login'),
    path('buyer/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('temp/', InventoryList.as_view()),
    path('temp/<int:pk>/', InventoryDetail.as_view()),
]