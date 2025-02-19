from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.db.models import Q
from users.models import CustomUser
from django.core.paginator import Paginator

@login_required
def home(request):
    if request.method == 'POST':
        content = request.POST['content']
        image = request.FILES.get('image')
        post = Post.objects.create(user=request.user, content=content, image=image)
        return redirect('home')
    
    friends = CustomUser.objects.filter(
        Q(friends_1__user2=request.user) | Q(friends_2__user1=request.user)
    )
    
    posts_list = Post.objects.filter(user__in=[request.user] + list(friends)).order_by('-created_at')
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'posts': posts})