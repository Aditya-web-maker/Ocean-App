from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList, name='home'),
    path('MyDrops/', views.MyPosts, name='MyDrops'),
    path('Aboutus/', views.AboutOcean, name='aboutocean'),
]