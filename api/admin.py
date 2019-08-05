from django.contrib import admin
from api.models import Product, Category, Tag


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
