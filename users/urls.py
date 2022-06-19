from django.contrib import admin
from django.urls import include, path

from users import views


urlpatterns = [
    path('join/', views.JoinView.as_view()),
    path('login/', views.UserAPIView.as_view()),
    path('logout/', views.UserAPIView.as_view()),
]
