from django.urls import path
from . import views

urlpatterns = [
    path('register/<str:role>/', views.register_view, name='register'),
    path('login/<str:role>/', views.login_view, name='login'),  # Ensure role parameter is included here
    path('logout/', views.logout_view, name='logout'),
    path('create_activity/', views.create_activity, name='create_activity'),
    path('activities/', views.activities, name='activities'),
    path('activity_list/', views.activity_list, name='activity_list'),
    path('organizers/', views.organizer_list, name='organizer_list'),
    path('edit_activity/<int:activity_id>/', views.edit_activity, name='edit_activity'), 
    path('organizer_details/', views.organizer_details, name='organizer_details'),
    path('create_organizer/', views.create_organizer, name='create_organizer'),
    path('organizer_home/', views.organizer_home, name='organizer_home'),
    path('organizer_summary/<int:organizer_id>/', views.organizer_summary, name='organizer_summary'),
    path('organizer/<int:organizer_id>/edit/', views.edit_organizer_summary, name='edit_organizer_summary'),
    path('create_participant/', views.create_participant, name='create_participant'),
    path('participant_home/', views.participant_home, name='participant_home'),
    path('participant_summary/<int:participant_id>/', views.participant_summary, name='participant_summary'),
    path('role_organizer/', views.role_organizer, name='role_organizer'),
    path('role_participant/', views.role_participant, name='role_participant'),
    path('', views.home_view, name='home'),
]