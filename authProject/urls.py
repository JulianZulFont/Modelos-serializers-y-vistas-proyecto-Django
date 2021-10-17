"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views


urlpatterns = [
    #URLS para peticiones del modelo usuario
     path('login/', TokenObtainPairView.as_view()),
     path('refresh/', TokenRefreshView.as_view()),
     path('user/', views.UserCreateView.as_view()),
     path('user/<int:pk>/', views.UserDetailView.as_view()),
     #URLS para peticiones del modelo transacción
     path('transaction/create/', views.TransactionsCreateView.as_view()),
     path('transaction/<int:user>/<int:pk>/', views.TransactionsDetailView.as_view()),
     path('transactions/<int:user>/<int:account>/', views.TransactionsAccountView.as_view()),
     path('transaction/update/<int:user>/<int:pk>/', views.TransactionsUpdateView.as_view()),
     path('transaction/remove/<int:user>/<int:pk>/', views.TransactionsDeleteView.as_view()),
     #URLS para peticiones del modelo factura
     path('factura/create/', views.FacturaCreateView.as_view()),
     path('factura/detail/<int:user>/<int:pk>/', views.FacturaDetailView.as_view()),
     path('factura/update/<int:user>/<int:pk>/', views.FacturaUpdateView.as_view()),
     path('factura/delete/<int:user>/<int:pk>/', views.FacturaDeleteView.as_view())
]