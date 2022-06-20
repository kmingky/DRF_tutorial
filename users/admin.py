from django.contrib import admin

from users.models import User as UserModel
from users.models import UserProfile as UserProfileModel
from users.models import Hobby as HobbyModel

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# admin 페이지에 user admin을 등록하고, userprofile 테이블을 user admin 페이지에서 같이 보고 설정 할 수 있도록 해주세요
class UserProfileInline(admin.StackedInline):
    model = UserProfileModel
    filter_horizontal = ["hobby"]

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'fullname')
    list_display_links = ('username', )
    list_filter = ('email', )
    search_fields = ('username', 'email')

    fieldsets = (
         ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date')}),
        ('permissions', {'fields': ('is_admin', 'is_active', )})

    )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("username", "join_date")
        else:
            return ("join_date")

    inlines = (
            UserProfileInline,
        )

# Register your models here.
admin.site.register(UserModel, UserAdmin)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)

