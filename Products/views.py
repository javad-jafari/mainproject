from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from Products.models import Product, ShopProduct
from Products.models import Category


# Create your views here.


class ProductDetailView(TemplateView):
    model = Product
    template_name = 'product.html'
    slug_url_kwarg = 'product_slug'


class CategoryDetailView(ListView):
    model = Category
    template_name = 'category.html'
    # slug_url_kwarg = 'category_slug'
    context_object_name = 'products'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        slug = self.kwargs.get('category_slug')
        category = get_object_or_404(Category.objects.filter(), slug=slug)
        context["products"] = Product.objects.filter(category=category)
        context["shopproducts"] = ShopProduct.objects.filter(product__category=category)
        context["categories"] = Category.objects.all()
        return context

    # def get_queryset(self):
    #     slug = self.kwargs.get('category_slug')
    #     category = get_object_or_404(Category.objects.filter(), slug=slug)
    #     products = Product.objects.filter(category=category)
    #     return products
