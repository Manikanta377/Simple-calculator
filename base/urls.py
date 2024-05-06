from django.urls import path
from . import views


urlpatterns = [
    path('',views.profile, name='profile'),
    path('calculate/', views.calculate, name='calculate'),
]
