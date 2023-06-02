from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.thread_list, name='thread_list'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('category/<int:category_id>/new_thread/', views.thread_create, name='thread_create'),
    path('thread/<int:thread_id>/new_post/', views.post_create, name='post_create'),
    path('post/<int:post_id>/new_comment/', views.comment_create, name='comment_create'),
]
