from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<uuid:pk>', views.userProfile, name='user_profile'),
    path('accout/login/', views.loginUser, name='login'),
    path('accout/logout/', views.logoutUser, name='logout'),
    path('accout/register/', views.registerUser, name='register'),
]
