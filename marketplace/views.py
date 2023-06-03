from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Item
from .forms import ItemForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'marketplace/category_list.html', {'categories': categories})

def item_list(request, category_id):
    items = Item.objects.filter(category_id=category_id)
    return render(request, 'marketplace/item_list.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'marketplace/item_detail.html', {'item': item})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('item_detail', item_id=new_item.id)
    else:
        form = ItemForm()
    return render(request, 'marketplace/item_form.html', {'form': form})

@login_required
def item_update(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', item_id=item_id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'marketplace/item_form.html', {'form': form})

@login_required
def item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('category_list')
