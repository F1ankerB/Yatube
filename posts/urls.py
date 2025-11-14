
from django.urls import path
from . import views
from .views import group_posts

urlpatterns = [
    path('', views.index),
    path('group_posts/<slug:slug>/', views.group_posts())
]
