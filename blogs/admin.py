from django.contrib import admin

from blogs.models import Category as CategoryModel
from blogs.models import Article as ArticleModel

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ArticleModel)