from django.urls import path
from . import views
from .views import baby_create_view, baby_detail_view, baby_update_view, welcome_page

app_name = "babies"

urlpatterns = [
    path('baby_create/', views.baby_create_view, name='baby_create'),
    path('<int:id>/', views.baby_detail_view, name='baby_detail'),
    path('<int:id>/update/', views.baby_update_view, name='baby_update'),
    path('welcome/<int:id>/', views.welcome_page, name='welcome_page'),
]
