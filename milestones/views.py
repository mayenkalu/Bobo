from django.shortcuts import render, redirect
from .forms import MilestoneLogForm
from .models import Milestone, Activity, NutritionGuide
from babies.models import Baby

from django.shortcuts import render, redirect
from .forms import MilestoneLogForm
from .models import Milestone, Activity, NutritionGuide
from babies.models import Baby

def log_milestone(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    if request.method == 'POST':
        form = MilestoneLogForm(request.POST, instance=baby, baby=baby)  # Pass the baby to the form
        if form.is_valid():
            form.save()
            return redirect('babies:baby_detail', id=baby.id)  # Note: change baby_id to id
    else:
        form = MilestoneLogForm(instance=baby, baby=baby)  # Pass the baby to the form
    return render(request, 'milestones/log_milestone.html', {'form': form})

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
