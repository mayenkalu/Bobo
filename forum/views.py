from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Thread, Post
from .forms import ThreadForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'forum/category_list.html', {'categories': categories})

@login_required
def thread_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'forum/thread_list.html', {'category': category})

@login_required
def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return render(request, 'forum/thread_detail.html', {'thread': thread})

@login_required
def thread_create(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.category = category
            thread.created_by = request.user
            thread.save()
            return redirect('forum:thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm()
    return render(request, 'forum/thread_form.html', {'form': form})

@login_required
def post_create(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            return redirect('forum:thread_detail', thread_id=thread.id)
    else:
        form = PostForm()
    return render(request, 'forum/post_form.html', {'form': form})

def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.created_by = request.user
            comment.save()
            return redirect('forum:thread_detail', thread_id=post.thread.id)
    else:
        form = CommentForm()
    return render(request, 'forum/comment_form.html', {'form': form})