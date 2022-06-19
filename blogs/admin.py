from django.contrib import admin

from blogs.models import Category as CategoryModel
from blogs.models import Article as ArticleModel
from blogs.models import Comment as CommentModel

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ArticleModel)
admin.site.register(CommentModel)