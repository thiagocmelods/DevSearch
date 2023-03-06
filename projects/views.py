from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = get_object_or_404(Project, id=pk)
    context = {'project': project}
    return render(request, 'projects/single-project.html', context)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')        
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)

def updateProject(request, pk):
    project = get_object_or_404(Project, id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')        
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)

def deleteProject(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'projects/delete-template.html', context)