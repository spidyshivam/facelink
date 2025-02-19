from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from friends.models import Friendship, FriendRequest  # Import friendship models
from .models import CustomUser
from posts.models import Post
from .models import CustomUser
from friends.models import Friendship
from posts.models import Post  # Ensure Post model is imported
from django.db.models import Q  # Import Q for complex queries


CustomUser = get_user_model()

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            # Handle form errors
            return render(request, 'register.html', {'form': form, 'errors': form.errors})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Invalid Username or Password'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile_update.html', {'form': form})

@login_required
def profile(request, username=None):
    if username:
        user = get_object_or_404(CustomUser, username=username)  # Public profile view
        is_own_profile = user == request.user
    else:
        user = request.user
        is_own_profile = True

    # Check if logged-in user and the profile user are friends
    is_friend = Friendship.objects.filter(
        Q(user1=request.user, user2=user) | Q(user1=user, user2=request.user)
    ).exists()

    # Check if friend request is sent
    friend_request = FriendRequest.objects.filter(
        sender=request.user, receiver=user, accepted=False
    ).first()  # Fetch request object

    is_friend_request_sent = friend_request is not None

    # Fetch posts only if the user is a friend or viewing their own profile
    posts = Post.objects.filter(user=user) if is_own_profile or is_friend else None

    return render(request, 'profile.html', {
        'user': user,
        'is_own_profile': is_own_profile,
        'is_friend': is_friend,
        'posts': posts,
        'is_friend_request_sent': is_friend_request_sent,
        'friend_request': friend_request,  # Include request for canceling
    })