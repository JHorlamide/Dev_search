from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, AccountForm, SkillForm
from .models import Profile
from .utiils import searchProfiles, paginateProfiles


def profiles(request):
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 3)
    context = {
        'profiles': profiles,
        'search_query': search_query,
        "custom_range": custom_range
    }
    return render(request, 'account/profiles.html', context)


def userProfile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    Topskills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        'profile': profile,
        'top_skills': Topskills,
        'other_skills': otherSkills
    }

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
            return redirect('account_update')
        else:
            messages.success(
                request, "An error occurred during registration, Please fill the form and try again")

    else:
        form = RegisterForm()

    context = {'page': 'register', 'form': form}
    return render(request, 'account/auth/login_register.html', context)


@login_required(login_url='login')
def account(request):
    profile = request.user.profile
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {
        "profile": profile,
        "topSkills": topSkills,
        "otherSkills": otherSkills
    }

    return render(request, 'account/account.html', context)


@login_required(login_url='login')
def profileUpdate(request):
    profile = request.user.profile
    form = AccountForm(instance=profile)

    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("user_account")
    context = {"form": form}
    return render(request, 'account/profile_form.html', context)


@login_required(login_url='login')
def addSkills(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill added successfully')
            return redirect("user_account")
        else:
            messages.error('Error creating skill. Please try again')
    else:
        form = SkillForm()

    context = {"page": "add_skills", "form": form}
    return render(request, 'account/skill_form.html', context)


@login_required(login_url='login')
def updateSkill(request, skillId):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=skillId)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully')
            return redirect("user_account")
        else:
            messages.error('Error updaing skill, please try again')

    context = {"page": "update_skill", "form": form}
    return render(request, "account/skill_form.html", context)


@login_required(login_url='login')
def deleteSkill(request, skillId):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=skillId)
    if request.method == 'POST':
        skill.delete()
        return redirect('user_account')
    context = {"object": skill}
    return render(request, 'delete_template.html', context)
