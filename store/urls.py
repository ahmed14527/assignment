from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, CategoryViewSet, ProductListAPIView, CategoryListAPIView

# Create a router and register the viewsets
router = DefaultRouter()
router.register('products', ProductsViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')

# The URL patterns
urlpatterns = [
    path('api/products/', ProductListAPIView.as_view(), name='product-list'),
    path('api/categories/', CategoryListAPIView.as_view(), name='category-list'),
]

# Extend the URL patterns with the router URLs
urlpatterns += router.urls