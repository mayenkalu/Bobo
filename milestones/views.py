from django.shortcuts import render, redirect
from .forms import MilestoneLogForm
from .models import Milestone, Activity, NutritionGuide
from babies.models import BabyProfile

def log_milestone(request, baby_id):
    baby = BabyProfile.objects.get(id=baby_id)
    form = MilestoneLogForm(request.POST, instance=baby)
    if form.is_valid():
        form.save()
    return redirect('baby_profile', baby_id=baby.id)

def view_expected_milestones(request, baby_id):
    baby = BabyProfile.objects.get(id=baby_id)
    expected_milestones = Milestone.objects.filter(month=baby.age_in_months)
    return render(request, 'expected_milestones.html', {'expected_milestones': expected_milestones, 'baby': baby})

def view_activities(request, baby_id):
    baby = BabyProfile.objects.get(id=baby_id)
    activities = Activity.objects.filter(month=baby.age_in_months)
    return render(request, 'activities.html', {'activities': activities, 'baby': baby})

def view_nutrition_guide(request, baby_id):
    baby = BabyProfile.objects.get(id=baby_id)
    nutrition_guide = NutritionGuide.objects.filter(month=baby.age_in_months)
    return render(request, 'nutrition_guide.html', {'nutrition_guide': nutrition_guide, 'baby': baby})
