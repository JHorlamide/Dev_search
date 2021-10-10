from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<uuid:pk>', views.userProfile, name='user_profile'),
    path('accout/login/', views.loginUser, name='login'),
    path('accout/logout/', views.logoutUser, name='logout'),
    path('accout/register/', views.registerUser, name='register'),
    path('account/my_profile/', views.account, name='user_account'),
    path('account/edit/', views.profileUpdate, name='account_update'),
    path('create-skill/', views.addSkills, name='create_skill'),
    path('update-skill/<uuid:skillId>/', views.updateSkill, name='update_skill'),
    path('delete/<uuid:skillId>/', views.deleteSkill, name='delete_skill'),
]
