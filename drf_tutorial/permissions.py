from email import message
from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone


class MyCustomPermission(BasePermission):

    message = '가입 후 3일 이상 지난 사용자만 사용할 수 있습니다.'

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        return bool(user.join_date < (timezone.now() - timedelta(days=3)))
