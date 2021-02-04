from django.urls import path, include
from .views import CategoryDetailView, ProductDetailView

urlpatterns = [
    path('category/<slug:category_slug>', CategoryDetailView.as_view(), name='category_detail'),
    # path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<slug:product_slug>/<slug:shop_slug>/', ProductDetailView.as_view(), name='product_detail'),
]
