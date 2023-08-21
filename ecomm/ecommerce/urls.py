# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.db import router
from django.urls import path,include

from ecommerce.models import registeration
from .serializers import demo_rest
from. import views
from ecommerce.views import demo_REST
from rest_framework import routers , serializers,viewsets

router = routers.DefaultRouter()
router.register(r'user',demo_REST,basename='MyModel')




urlpatterns = [
    path('',views.index, name = 'home'),
    path('contact/',views.contact , name= 'contact'),
    path('signup/',views.signup , name = 'signup'),
    path('login_info/',views.login_info, name="login_info"),
    path('cart/',views.cart, name ='cart' ),
    path('checkout/', views.checkout, name = "checkout"),
    path('logout/',views.logout, name = 'logout'),
    path('ordersdtls/',views.ordersdtls,name='ordersdtls'),
    path('h/',include(router.urls)),
    path('api_auth/',include('rest_framework.urls',namespace='rest_framework')),

]
