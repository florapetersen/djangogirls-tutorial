from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #name='post_list' is the name of the URL used to identify the view
]