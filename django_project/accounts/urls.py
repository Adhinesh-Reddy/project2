from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('rent/', views.rentPage, name = 'rent'),
    path('rentHouse/', views.rentHousePage, name = 'rentHouse'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profilePage, name='profile')
]