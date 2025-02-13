from django.urls import path
from .views import send_friend_request, accept_friend_request, reject_friend_request, friends_list

urlpatterns = [
    path('', friends_list, name='friends_list'),
    path('add/<str:username>/', send_friend_request, name='send_friend_request'),
    path('accept/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('reject/<int:request_id>/', reject_friend_request, name='reject_friend_request'),
]
