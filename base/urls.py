from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<str:pk>/', views.update_room, name='update_room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete_room'),
    path('delete_message/<str:pk>/', views.delete_message, name='delete_message'),
]
