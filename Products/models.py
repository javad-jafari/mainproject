from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from Accounts.models import Shop
# Create your models here.

User = get_user_model()

class Category(models.Model):
    name = models.CharField(_('name'),max_length=50)
    slug = models.SlugField(_('slug'))
    detail = models.TextField(_('detail'))
    image = models.ImageField(_('image'),upload_to='/category/image/')
    parent = models.ForeignKey(
        'self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True,
        related_name='children', related_query_name='children')
    

class Brand(models.Model):
    name = models.CharField(_('name'),max_length=50)
    detail = models.TextField(_('detail'))
    image = models.ImageField(_('image'),upload_to='/brand/image/')

class Product(models.Model):
    name = models.CharField(_('name'),max_length=50)
    slug = models.SlugField(_('slug'))
    detail = models.TextField(_('detail'))
    image = models.ImageField(_('image'),upload_to='/product/image/')
    brand = models.ForeignKey(Brand,related_name='Product', related_query_name='Product', verbose_name=_(
        "brand"), on_delete=models.CASCADE))
    category = models.ForeignKey(Category, related_name='products', verbose_name=_(
        "Category"), on_delete=models.SET_NULL, null=True, blank=True)

class ProductMeta(models.Model):
    product= models.ForeignKey(Product,related_name='ProductMeta', related_query_name='ProductMeta',
     verbose_name=_("Product"), on_delete=models.CASCADE)
    label = models.CharField(_('label'),max_length=50)
    value = models.IntegerField(_('value'))

class Image(models.Model):
    product= models.ForeignKey(Product,related_name='Images', related_query_name='Images', verbose_name=_(
        "Product"), on_delete=models.CASCADE))
    image = models.ImageField(_('image'),upload_to='/image/image/')

class Comment(models.Model):
    content = models.TextField(_("Content"))
    product = models.ForeignKey(Product, related_name='comments', related_query_name='comments', verbose_name=_(
        "Product"), on_delete=models.CASCADE)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_(
        "Author"), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("confirm"), default=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-create_at']

class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop,related_name='ShopProducts', related_query_name='ShopProducts', verbose_name=_(
        "ShopProduct"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='ShopProducts', related_query_name='ShopProducts', verbose_name=_(
        "ShopProduct"), on_delete=models.CASCADE)
    price = models.FloatField(_('price'))
    quantity = models.IntegerField(_('quantity'))