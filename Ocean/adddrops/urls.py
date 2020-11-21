from django.urls import path
from . import views
 
app_name = 'adddrops'
 
urlpatterns = [
    path('adddrop/', views.adpost_view.as_view(), name='adddrop'),
]