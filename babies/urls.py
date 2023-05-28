from django.urls import path
from . import views
from .views import baby_create_view, baby_detail_view, baby_update_view, welcome_page

urlpatterns = [
    path('baby_create/', baby_create_view, name='baby_create'),
    path('babies/<int:id>/', baby_detail_view, name='baby_detail'),
    path('babies/<int:id>/update/', baby_update_view, name='update'),
    path('welcome/<int:id>/', welcome_page, name='welcome_page'),
    # ...
]
