from django.contrib import admin

# Register your models here.
from .models import ProductTemplate, ProductProduct, ProductCategory

admin.site.register(ProductTemplate)
admin.site.register(ProductProduct)
admin.site.register(ProductCategory)