from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView
from Products.models import Product, ShopProduct, Comment, like
from Products.models import Category
import json

# Create your views here.


class ProductDetailView(DetailView):
    model = ShopProduct
    template_name = 'product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_object(self):
        slug1 = self.kwargs.get('product_slug')
        slug2 = self.kwargs.get('shop_slug')
        item = get_object_or_404(ShopProduct, product__slug=slug1, shop__slug=slug2)
        item.incrementViewCount()
        return item

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
        # context["products"] = Product.objects.filter(category=category)
        context["shopproducts"] = ShopProduct.objects.filter(product__category=category)
        context["categories"] = Category.objects.all()
        return context


@csrf_exempt
def like_comment(request):
    data = json.loads(request.body)
    user = request.user
    try:
        comment = Comment.objects.get(id=data['comment_id'])
    except Comment.DoesNotExist:
        return HttpResponse('bad request', status=404)
    try:
        comment_like = like.objects.get(author=user, comment=comment)
        comment_like.condition = data['condition']
        comment_like.save()
    except like.DoesNotExist:
        like.objects.create(author=user, condition=data['condition'], comment=comment)
    result = {'like_count': comment.like_count, 'dislike_count': comment.dislike_count}

    return HttpResponse(json.dumps(result), status=201)


@csrf_exempt
def create_comment(request):
    data = json.loads(request.body)
    user = request.user
    try:
        comment = Comment.objects.create(post_id=data['post_id'], content=data['content'], author=user)
        result = {"comment_id": comment.id, "content": comment.content, 'dislike_count': 0, 'like_count': 0,
                  'full_name': user.get_full_name()}
        return HttpResponse(json.dumps(result), status=201)
    except:
        result = {"error": 'error'}
        return HttpResponse(json.dumps(result), status=400)
