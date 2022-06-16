from django.contrib import admin

from users.models import User as UserModel

# Register your models here.
admin.site.register(UserModel)