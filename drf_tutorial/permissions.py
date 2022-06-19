from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone


class MyCustomPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        return bool(user.join_date < (timezone.now() - timedelta(days=3)))
