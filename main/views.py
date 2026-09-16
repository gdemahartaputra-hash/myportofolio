from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education, Project
from main.forms import ProjectForm


def show_main(request):
    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "npm": "2506549051",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "I'm a dynamic individual with a deep passion for technology, business, and the arts. With my strong foundation in programming and mathematics, I leverage my technical expertise to build impactful solutions. My musical background infuses my work with creativity, allowing me to tackle challenges and improve my problem solving skill exponentially. I am relentless in my pursuit of excellence, always seeking opportunities to grow and make a positive impact."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "education_list": Education.objects.all().order_by('-started_year'),
    }
    return render(request, "education.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Burhan",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")