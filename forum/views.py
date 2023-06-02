from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Thread, Post
from .forms import ThreadForm, PostForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'forum/category_list.html', {'categories': categories})

def thread_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'forum/thread_list.html', {'category': category})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return render(request, 'forum/thread_detail.html', {'thread': thread})

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
