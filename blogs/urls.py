from django.contrib import admin
from django.urls import include, path

from blogs import views


urlpatterns = [
    path('', views.ArticleView.as_view()),
]
