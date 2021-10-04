from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile

from .forms import RegisterForm
from .forms import LoginForm


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'account/profiles.html', context)


def userProfile(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    Topskills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'top_skills': Topskills,
               'other_skills': otherSkills}
    return render(request, 'account/user_profile.html', context)


def loginUser(request):
    context = {'page': 'login'}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exists")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username Or Password is incorrect")
    return render(request, 'account/auth/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, "Logout success")
    return redirect('login')


def registerUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "You've been registered successfully")
            login(request, user)
            return redirect('login')
        else:
            messages.success(request, "An error occurred during registration")

    else:
        form = RegisterForm()

    context = {'page': 'register', 'form': form}
    return render(request, 'account/auth/login_register.html', context)
