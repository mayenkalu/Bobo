from django.shortcuts import render, redirect
from .forms import MilestoneLogForm
from .models import Milestone, Activity, NutritionGuide
from babies.models import Baby

from django.shortcuts import render, redirect
from .forms import MilestoneLogForm
from .models import Milestone, Activity, NutritionGuide
from babies.models import Baby
from itertools import groupby


from django.contrib import messages

def log_milestone(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    milestones = Milestone.objects.filter(month=baby.age_in_months)
    logged_milestones = list(baby.logged_milestones.values_list('id', flat=True))

    grouped_milestones = {}
    for milestone in milestones:
        grouped_milestones.setdefault(milestone.area, []).append((milestone.id, milestone.description))

    if request.method == 'POST':
        form = MilestoneLogForm(request.POST, instance=baby, baby=baby, grouped_milestones=grouped_milestones)
        if form.is_valid():
            form.save()
            messages.success(request, 'Milestones logged successfully.')
            return redirect('milestones:log_milestone', baby_id=baby.id)
    else:
        form = MilestoneLogForm(instance=baby, baby=baby, grouped_milestones=grouped_milestones, initial={'logged_milestones': logged_milestones})

    return render(request, 'milestones/log_milestone.html', {'form': form, 'grouped_milestones': grouped_milestones, 'logged_milestones': logged_milestones})







def view_expected_milestones(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    expected_milestones = Milestone.objects.filter(month=baby.age_in_months)
    return render(request, 'milestones/view_expected_milestones.html', {'expected_milestones': expected_milestones, 'baby': baby})

def view_activities(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    activities = Activity.objects.filter(month=baby.age_in_months)
    return render(request, 'milestones/activities.html', {'activities': activities, 'baby': baby})

def view_nutrition_guide(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    nutrition_guide = NutritionGuide.objects.filter(month=baby.age_in_months)
    return render(request, 'milestones/nutrition_guide.html', {'nutrition_guide': nutrition_guide, 'baby': baby})
