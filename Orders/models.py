from Products.models import ShopProduct
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='orders', related_query_name='orders', verbose_name=_(
        "user"),on_delete=models.CASCADE) 
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    discription = models.TextField(_('discription'))


class Payment(models.Model):

    order = models.ForeignKey(Order,related_name='paymentsorder', related_query_name='paymentsorder', verbose_name=_(
        "order"), on_delete=models.CASCADE)

    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='paymentsuser', related_query_name='paymentsuser', verbose_name=_(
    "user"), on_delete=models.CASCADE)

    amount = models.IntegerField(_('amount'))

class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='baskets', related_query_name='baskets', verbose_name=_(
    "user"), on_delete=models.CASCADE)

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket,related_name='itemsbasket', related_query_name='itemsbasket', verbose_name=_(
    "basket"), on_delete=models.CASCADE)
    shop_product = models.ForeignKey(ShopProduct,related_name='itemsshop_product', related_query_name='itemsshop_product', verbose_name=_(
    "shop_product"), on_delete=models.CASCADE)

class OrderShopProduct(models.Model):
    order = models.ForeignKey(Order,related_name='Orderorder', related_query_name='Orderorder', verbose_name=_(
        "order"), on_delete=models.CASCADE)
    
    shop_product = models.ForeignKey(Order,related_name='Ordershop_product', related_query_name='Ordershop_product', verbose_name=_(
        "shop_product"), on_delete=models.CASCADE)    
    count = models.IntegerField(_('count'))