from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rf.views import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls
