from django.urls import path, include
from .views import CategoryDetailView, ProductDetailView, like_comment, create_comment

urlpatterns = [
    path('category/<slug:category_slug>', CategoryDetailView.as_view(), name='category_detail'),
    # path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<slug:product_slug>/<slug:shop_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('like_comment/', like_comment, name='like_comment'),
    path('comments/', create_comment, name='add_comment'),
]
