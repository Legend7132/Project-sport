from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('video/', views.video_list, name="video_list"),
    path('contacts/', views.contacts, name='contacts'),
]