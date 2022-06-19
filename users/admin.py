from django.contrib import admin

from users.models import User as UserModel
from users.models import UserProfile as UserProfileModel
from users.models import Hobby as HobbyModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)