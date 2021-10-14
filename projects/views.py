from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from . models import Project
from . forms import ProjectForm, ReviewForm
from . utils import searchProject, paginateProject


def projects(request):
    projects, search_query = searchProject(request)

    custom_range, projects = paginateProject(request, projects, 3)

    context = {
        'projects': projects,
        "search_query": search_query,
        "custom_range": custom_range
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'projects/single_project.html', {'project': project})


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateProject(request, projectId):
    profile = request.user.profile
    project = profile.project_set.get(pk=projectId)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def deleteProject(request, projectId):
    profile = request.user.profile
    project = profile.project_set.get(pk=projectId)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)


@login_required(login_url="login")
def addReview(request, projectId):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)

    context = {"form": form}
    return render(request, 'single_project.html', context)
