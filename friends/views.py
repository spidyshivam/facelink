from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import FriendRequest, Friendship

CustomUser = get_user_model()

@login_required
def send_friend_request(request, username):
    receiver = get_object_or_404(CustomUser, username=username)
    if request.user != receiver and not Friendship.objects.filter(user1=request.user, user2=receiver).exists():
        FriendRequest.objects.get_or_create(sender=request.user, receiver=receiver)
    return redirect('user_profile', username=username)

@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user)
    friend_request.accepted = True
    friend_request.save()
    Friendship.objects.create(user1=friend_request.sender, user2=friend_request.receiver)
    Friendship.objects.create(user1=friend_request.receiver, user2=friend_request.sender)
    friend_request.delete()
    return redirect('profile')

@login_required
def reject_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user)
    friend_request.delete()
    return redirect('profile')

@login_required
def friends_list(request):
    search_query = request.GET.get('search')
    if search_query:
        return redirect('find_friends')
    friends = Friendship.objects.filter(user1=request.user).values_list('user2', flat=True)
    friends = CustomUser.objects.filter(id__in=friends)
    friend_requests = FriendRequest.objects.filter(receiver=request.user, accepted=False)
    return render(request, 'friends_list.html', {'friends': friends, 'requests' : friend_requests})

@login_required
def find_friends(request):
    search_query = request.GET.get('search', '')

    if search_query:
         users = CustomUser.objects.filter(username__icontains=search_query).exclude(id=request.user.id)
    else:
        users = CustomUser.objects.none()
    return render(request, 'find_friends.html', {'users': users, 'search_query': search_query})

@login_required
def unfriend(request, username):
    friend = get_object_or_404(CustomUser, username=username)
    Friendship.objects.filter(user1=request.user, user2=friend).delete()
    Friendship.objects.filter(user1=friend, user2=request.user).delete()
    return redirect('friends_list')
@login_required
def cancel_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, sender=request.user)
    receiver_username = friend_request.receiver.username  # Get receiver's username before deleting
    friend_request.delete()
    return redirect('user_profile', username=receiver_username)