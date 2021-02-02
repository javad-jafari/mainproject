from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from Products.models import Product, ShopProduct
from Products.models import Category


# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

    def get_object(self):
        slug1 = self.kwargs.get('product_slug')
        # slug2 = self.kwargs.get('shop_slug')

        # return ShopProduct.objects.filter(product__slug=slug1, shop__slug=slug2)
        return get_object_or_404(ShopProduct, product__slug=slug1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CategoryDetailView(ListView):
    model = Category
    template_name = 'category.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
