# centralbookings/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm, OrganizerForm, ContactPersonForm
from .models import CustomUser, Organizer, ContactPerson

def home_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'organizer':
            return redirect('role_organizer')
        elif role == 'participant':
            return redirect('role_participant')
    return render(request, 'home.html')

def role_organizer(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'login':
            return redirect('login')
        elif action == 'register':
            return redirect('register')
    return render(request, 'role_organizer.html')

def role_participant(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'login':
            return redirect('login')
        elif action == 'register':
            return redirect('register')
    return render(request, 'role_participant.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == CustomUser.ORGANIZER:
                return redirect('create_organizer')
            else:
                return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == CustomUser.ORGANIZER:
                return redirect('organizer_home')
            else:
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

def create_organizer(request):
    if request.method == 'POST':
        organizer_form = OrganizerForm(request.POST)
        contact_form = ContactPersonForm(request.POST)
        if organizer_form.is_valid() and contact_form.is_valid():
            organizer = organizer_form.save()
            contact = contact_form.save(commit=False)
            contact.Organizer_ID = organizer
            contact.save()
            return redirect('organizer_summary', organizer_id=organizer.Organizer_ID)
    else:
        organizer_form = OrganizerForm()
        contact_form = ContactPersonForm()
    return render(request, 'create_organizer.html', {'organizer_form': organizer_form, 'contact_form': contact_form})

def organizer_home(request):
    return render(request, 'organizer_home.html')

def organizer_summary(request, organizer_id):
    organizer = Organizer.objects.get(pk=organizer_id)
    contact = ContactPerson.objects.get(Organizer_ID=organizer)
    return render(request, 'organizer_summary.html', {'organizer': organizer, 'contact': contact})
