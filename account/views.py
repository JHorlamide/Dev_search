from django.shortcuts import render, get_object_or_404
from .models import Profile


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
