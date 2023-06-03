from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.item_list, name='item_list'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/new/', views.item_create, name='item_create'),
    path('item/<int:item_id>/edit/', views.item_update, name='item_update'),
    path('item/<int:item_id>/delete/', views.item_delete, name='item_delete'),
]
