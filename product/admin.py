from django.contrib import admin

from .models import Category, Product, ProductComment

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductComment)
