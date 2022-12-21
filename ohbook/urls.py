from django.urls import path
from . import views
from ohbook.views import detail_feed
from ohbook.views import new_feed
from ohbook.views import remove_feed, edit_feed, fail

urlpatterns = [
    path('', views.index),
    path('play/', views.play),
    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/remove', remove_feed),
    path('feed/<pk>/edit', edit_feed),
    path('new/', new_feed),
    path('fail/', fail),
]