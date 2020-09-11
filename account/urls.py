from django.urls import path

from account import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]

