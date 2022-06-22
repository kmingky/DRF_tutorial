from django.contrib import admin

from .models import Product as ProductModel
from .models import ProductCategory as ProductCategoryModel
from .models import ProductOption as ProductOptionModel
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(ProductCategoryModel)
admin.site.register(ProductOptionModel)