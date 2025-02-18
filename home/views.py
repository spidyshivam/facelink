from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        content = request.POST['content']
        image = request.FILES.get('image')
        post = Post.objects.create(user=request.user, content=content, image=image)
        return redirect('home')
    posts = Post.objects.filter(user__in=[request.user] + list(request.user.friends.all())).order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})
