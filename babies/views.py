from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BabyForm
from .models import Baby
from django.contrib.auth.decorators import login_required

@login_required
def baby_create_view(request):
    if request.method == 'POST':
        form = BabyForm(request.POST, request.FILES)
        if form.is_valid():
            baby = form.save(commit=False)
            baby.user = request.user
            baby.save()
            return redirect('welcome_page', baby.id)
            #return redirect('babies:detail', baby.id)
    else:
        form = BabyForm()
    return render(request, 'babies/baby_form.html', {'form': form})

@login_required
def welcome_page(request, id):
    baby = get_object_or_404(Baby, id=id)
    return render(request, 'babies/welcome_page.html', {'baby': baby})


@login_required
def baby_detail_view(request, id):
    baby = get_object_or_404(Baby, id=id)
    return render(request, 'babies/baby_detail.html', {'baby': baby})

@login_required
def baby_update_view(request, id):
    baby = get_object_or_404(Baby, id=id)
    if request.method == 'POST':
        form = BabyForm(request.POST, request.FILES, instance=baby)
        if form.is_valid():
            form.save()
            return redirect('babies:detail', baby.id)
    else:
        form = BabyForm(instance=baby)
    return render(request, 'babies/baby_form.html', {'form': form})
