from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from . models import Project
from . forms import ProjectForm
from . utils import searchProject

def projects(request):
    projects, search_query = searchProject(request)

    page = request.GET.get('page')
    project_per_page = 3
    paginator = Paginator(projects, project_per_page)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    custom_range = range(1, 20)

    context = {
        'projects': projects, 
        "search_query": search_query, 
        "paginator": paginator, 
        "custome_range": custom_range
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

