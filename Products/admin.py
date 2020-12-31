from django.contrib import admin

from .models import Product,ShopProduct, Category, Comment,Brand


# Register your models here.


class ChildrenItemInline(admin.TabularInline):
    model = Category
    fields = (
        'name', 'slug'
    )
    extra = 1
    show_change_link = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'parent')
    search_fields = ('slug', 'name')
    list_filter = ('parent',)
    inlines = [
        ChildrenItemInline,
    ]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','brand', 'category', )
    search_fields = ('name',)
    list_filter = ('brand', 'category', 'name')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_confirmed', 'author')
    search_fields = ('content',)
    list_filter = ('is_confirmed',)
    date_hierarchy = 'create_at'


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Like)

