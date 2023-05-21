from django.urls import path
from .views import signup_view, login_view, home_view
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('delete_account/', views.delete_account_view, name='delete_account'),
    path('delete_account_confirm/', views.delete_account_confirm_view, name='delete_account_confirm'),
]
