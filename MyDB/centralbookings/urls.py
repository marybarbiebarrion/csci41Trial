# centralbookings/urls.py
from django.urls import path
# from .views import register_view, login_view, logout_view, home_view
from . import views

# urlpatterns = [
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('create_organizer/', views.create_organizer, name='create_organizer'),
#     path('organizer_summary/<int:organizer_id>/', views.organizer_summary, name='organizer_summary'),
#     path('', views.home_view, name='home'),
# ]

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_organizer/', views.create_organizer, name='create_organizer'),
    path('organizer_home/', views.organizer_home, name='organizer_home'),  # Add this line
    path('organizer_summary/<int:organizer_id>/', views.organizer_summary, name='organizer_summary'),
    path('role_organizer/', views.role_organizer, name='role_organizer'),
    path('role_participant/', views.role_participant, name='role_participant'),
    path('', views.home_view, name='home'),
]