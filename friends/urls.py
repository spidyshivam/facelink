from django.urls import path
from .views import send_friend_request, accept_friend_request, reject_friend_request, friends_list, unfriend, cancel_friend_request, find_friends

urlpatterns = [
    path('', friends_list, name='friends_list'),
    path('add/<str:username>/', send_friend_request, name='send_friend_request'),
    path('accept/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('reject/<int:request_id>/', reject_friend_request, name='reject_friend_request'),
    path('unfriend/<str:username>/', unfriend, name='unfriend'),
    path('cancel/<int:request_id>/', cancel_friend_request, name='cancel_friend_request'),
    path('find/', find_friends, name='find_friends'),
]
