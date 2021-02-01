from django.db import models
from django.db.models.base import Model
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from Accounts.models import Shop
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(_('slug'),unique=True)
    detail = models.TextField(_('detail'))
    image = models.ImageField(_('image'), upload_to='Product/Category/image')
    parent = models.ForeignKey(
        'self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True,
        related_name='children', related_query_name='children')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class Brand(models.Model):
    name = models.CharField(_('name'), max_length=50)
    detail = models.TextField(_('detail'))
    image = models.ImageField(_('image'), upload_to='Product/Brand/image')

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(_('slug'),unique=True)
    detail = models.TextField(_('detail'))
    image = models.ImageField(_('image'), upload_to='Product/Product/image')
    brand = models.ForeignKey(Brand, related_name='Product', related_query_name='Product', verbose_name=_(
        "brand"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', verbose_name=_(
        "Category"), on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})


class ProductMeta(models.Model):
    product = models.ForeignKey(Product, related_name='ProductMeta', related_query_name='ProductMeta',
                                verbose_name=_("Product"), on_delete=models.CASCADE)
    label = models.CharField(_('label'), max_length=50)
    value = models.IntegerField(_('value'))

    class Meta:
        verbose_name = _('ProductMeta')
        verbose_name_plural = _('ProductMetas')

    def __str__(self):
        return self.product.name


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='Images', related_query_name='Images', verbose_name=_(
        "Product"), on_delete=models.CASCADE)
    image = models.ImageField(_('image'), upload_to='Product/Image/image')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.product.name


class Comment(models.Model):
    content = models.TextField(_("Content"))
    product = models.ForeignKey(Product, related_name='comments', related_query_name='comments', verbose_name=_(
        "Product"), on_delete=models.CASCADE)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        "Author"), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("confirm"), default=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-create_at']


class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop, related_name='Shops', related_query_name='Shops', verbose_name=_(
        "Shops"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='ShopProducts', related_query_name='ShopProducts', verbose_name=_(
        "ShopProduct"), on_delete=models.CASCADE)
    price = models.FloatField(_('price'))
    quantity = models.IntegerField(_('quantity'))

    class Meta:
        verbose_name = _('ShopProduct')
        verbose_name_plural = _('ShopProducts')

    def __str__(self):
        return self.shop.name


class like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='userlikes', related_query_name='userlikes',
                             verbose_name=_(
                                 "user"), on_delete=models.SET_NULL, null=True)

    product = models.ForeignKey(Product, related_name='Productlikes', related_query_name='Productlikes', verbose_name=_(
        "product"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')

    def __str__(self):
        return self.user.mobile
