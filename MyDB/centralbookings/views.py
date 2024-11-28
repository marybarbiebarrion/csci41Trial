from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm, OrganizerForm, ContactPersonForm, ParticipantForm, ActivityForm
from .models import CustomUser, Organizer, ContactPerson, Participant, UserOrganizer, Activity

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
            return redirect('login', role='organizer')
        elif action == 'register':
            return redirect('register', role='organizer')
    return render(request, 'role_organizer.html')

def role_participant(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'login':
            return redirect('login', role='participant')
        elif action == 'register':
            return redirect('register', role='participant')
    return render(request, 'role_participant.html')

def register_view(request, role):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if role == 'organizer':
            organizer_form = OrganizerForm(request.POST)
            contact_form = ContactPersonForm(request.POST)
            if user_form.is_valid() and organizer_form.is_valid() and contact_form.is_valid():
                user = user_form.save(commit=False)
                user.role = CustomUser.ORGANIZER
                user.save()
                login(request, user)
                organizer = organizer_form.save(commit=False)
                organizer.user = user
                organizer.save()
                contact = contact_form.save(commit=False)
                contact.Organizer_ID = organizer
                contact.save()
                UserOrganizer.objects.create(user=user, organizer=organizer)
                return redirect('organizer_summary', organizer_id=organizer.Organizer_ID)
            else:
                return render(request, 'organizer_register.html', {
                    'user_form': user_form,
                    'organizer_form': organizer_form,
                    'contact_form': contact_form,
                    'back_url': 'role_organizer'
                })
        elif role == 'participant':
            participant_form = ParticipantForm(request.POST)
            if user_form.is_valid() and participant_form.is_valid():
                user = user_form.save(commit=False)
                user.role = CustomUser.PARTICIPANT
                user.save()
                login(request, user)
                participant = participant_form.save(commit=False)
                participant.user = user
                participant.save()
                return redirect('participant_summary', participant_id=participant.ID_Number)
            else:
                return render(request, 'participant_register.html', {
                    'user_form': user_form,
                    'participant_form': participant_form,
                    'back_url': 'role_participant'
                })
    else:
        user_form = CustomUserCreationForm()
        if role == 'organizer':
            organizer_form = OrganizerForm()
            contact_form = ContactPersonForm()
            return render(request, 'organizer_register.html', {
                'user_form': user_form,
                'organizer_form': organizer_form,
                'contact_form': contact_form,
                'back_url': 'role_organizer'
            })
        elif role == 'participant':
            participant_form = ParticipantForm()
            return render(request, 'participant_register.html', {
                'user_form': user_form,
                'participant_form': participant_form,
                'back_url': 'role_participant'
            })

def login_view(request, role):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(f"Logging in user: {user.username}, Role: {user.role}")  # Debugging statement
            login(request, user)
            if user.role == CustomUser.ORGANIZER:
                return redirect('organizer_home')
            elif user.role == CustomUser.PARTICIPANT:
                return redirect('participant_home')
            else:
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form, 'back_url': f'role_{role}'})


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
    try:
        user_organizer = UserOrganizer.objects.get(user=request.user)
        organizer = user_organizer.organizer
    except UserOrganizer.DoesNotExist:
        # Redirect to a page where users can create or link their organizer profile
        return redirect('create_organizer')  # Assuming you have a view to create an organizer

    return render(request, 'organizer_home.html', {'organizer': organizer})

def organizer_summary(request, organizer_id):
    organizer = Organizer.objects.get(pk=organizer_id)
    contact = ContactPerson.objects.get(Organizer_ID=organizer)
    return render(request, 'organizer_summary.html', {'organizer': organizer, 'contact': contact, 'back_url': 'home'})

def create_participant(request):
    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)
        if participant_form.is_valid():
            participant = participant_form.save()
            return redirect('participant_summary', participant_id=participant.ID_Number)
    else:
        participant_form = ParticipantForm()
    return render(request, 'create_participant.html', {'participant_form': participant_form})

def participant_home(request):
    return render(request, 'participant_home.html')

def participant_summary(request, participant_id):
    participant = Participant.objects.get(pk=participant_id)
    return render(request, 'participant_summary.html', {'participant': participant, 'back_url': 'home'})

def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.Organizer = request.user.organizer
            activity.save()
            return redirect('activities')
    else:
        form = ActivityForm()
    return render(request, 'create_activity.html', {'form': form})

def activities(request):
    activities = request.user.organizer.activities.all()
    return render(request, 'activities.html', {'activities': activities})

def organizer_details(request):
    organizer = request.user.organizer
    contact_person = organizer.contactperson_set.first()
    activities = organizer.activities.all()
    return render(request, 'organizer_details.html', {
        'organizer': organizer,
        'contact_person': contact_person,
        'activities': activities,
    })