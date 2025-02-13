from django.urls import path
from .views import register, user_login, user_logout, profile, profile_update

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('<str:username>/', profile, name='user_profile'),
    path('profile/edit/', profile_update, name='profile_update'),
]
