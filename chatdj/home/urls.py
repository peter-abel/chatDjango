from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name='home' ),
    path('save_message/', views.save_message, name='save_message'),


]