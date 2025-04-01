from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    form = CommentForm()

    context = {
        'posts': posts,
        'form': form,
    }

    return render(request, 'index.html', context)
@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

@login_required
def comment_create(request, post_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
        return redirect('posts:index')

@login_required
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)

    # if post in user.like_posts.all():
    if user in post.like_users.all(): # 이 게시물에 좋아요 버튼을 누른 사람들의 목록이 생성.(누른 상태)
        # user.like_posts.remove(post)
        post.like_users.remove(user)
        
    else: # (안 누른 상태)
        # user.like_posts.add(post) / user 부터 시작하냐 post 부터 시작하냐의 차이 
        post.like_users.add(user)

    return redirect('posts:index')