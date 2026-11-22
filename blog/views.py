from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from blog.models import Post, Tag, Comment

# Create your views here.
def home(request):
    # if request.user.is_authenticated:
    #     return redirect('blog:dashboard')
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'blog/home.html', context=context)

@login_required
def dashboard_view(request):
    blogs = Post.objects.filter(author=request.user)
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/dashboard.html', context = context)

@login_required
def create_post_view(request): #CREATE
    available_tags = list(
        Tag.objects.values("id", "name")
    )
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        tags = request.POST.getlist('tags')  # Get the selected tags as a list

        if not title or not content:
            messages.error(request, 'Title and content are required.')
            return redirect('blog:create_blog')
        
        post = Post.objects.create(author=request.user, title=title, content=content, image=image)
        post.tags.set(tags)  # Set the selected tags for the post

        messages.success(request, 'Blog added successfully!')

        return redirect('blog:dashboard')

    context = {
        'available_tags': available_tags
    }

    return render(request, 'blog/add_blog.html', context=context)

def post_list_view(request): #READ
    blogs = Post.objects.all()
    # Get all tags
    tags = Tag.objects.all()
    context = {
        'blogs': blogs,
        'tags': tags
    }
    return render(request, 'blog/home.html', context=context)

def post_detail_view(request, blog_id):
    post =  get_object_or_404(Post, pk = blog_id)
    comments = post.comments.all()
    tags = post.tags.all()
    context = {
        'post': post,
        'comments': comments,
        'tags': tags
    }
    return render(request, 'blog/blog_detail.html', context=context)

@login_required
def post_update_view(request, blog_id): #UPDATE
    post = get_object_or_404(Post, pk = blog_id)
    print("POST DATA:", request.POST)
    print("TITLE:", request.POST.get('title'))
    print("CONTENT:", request.POST.get('content'))
    print(request.POST)

    if post.author != request.user:
        messages.error(request, 'You are not authorized to update this blog.')
        return redirect('blog:home')
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        messages.success(request, 'Blog updated successfully!')

        return redirect('blog:dashboard')
    
    return render(request, 'blog/blog_update.html', context={'post': post})


@login_required
def post_delete_view(request, blog_id): #DELETE
    post = get_object_or_404(Post, id = blog_id)
    if post.author != request.user:
        messages.error(request, 'You are not authorized to delete this blog.')
        return redirect('blog:dashboard')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog deleted successfully!')
        return redirect('blog:dashboard')

    return render(request, 'blog/blog_detail.html', context={'post': post})

@login_required
def add_comment_view(request, blog_id): #create comment
    post = get_object_or_404(Post, id = blog_id)
    author = request.user
    content = request.POST.get('content')

    if post.author == author:
        messages.error(request, 'You cannot comment on your own blog.')
        return redirect('blog:blog_detail', blog_id=blog_id)
    
    if request.method == 'POST':
        comment = Comment.objects.create(author=author, post=post, content=content)
        messages.success(request, 'Comment added successfully!')
        return redirect('blog:blog_detail', blog_id=blog_id)
    
    return render(request, 'blog/add_comment.html', context={'post': post})

