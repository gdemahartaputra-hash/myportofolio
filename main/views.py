import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied 

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education, Project
from main.forms import ProjectForm, ExperienceForm, EducationForm


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "npm": "2506549051",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "I'm a dynamic individual with a deep passion for technology, business, and the arts. With my strong foundation in programming and mathematics, I leverage my technical expertise to build impactful solutions. My musical background infuses my work with creativity, allowing me to tackle challenges and improve my problem solving skill exponentially. I am relentless in my pursuit of excellence, always seeking opportunities to grow and make a positive impact."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

# Experience Section

def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [e.object for e in experiences]
    is_editor = request.user.is_authenticated and request.user.groups.filter(name="Editor").exists()

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "experience_list": experiences,
        "is_editor": is_editor,
    }
    return render(request, "experience.html", context)

def get_experience_json(request):
    experiences = Experience.objects.all()
    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

@login_required(login_url="/login/")
def create_experience(request):

    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    is_editor = request.user.groups.filter(name="Editor").exists()
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

# Education Section

def show_education(request):
    json_response = get_education_json(request)
    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [e.object for e in educations]
    educations.sort(key=lambda e: e.started_year, reverse=True)

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "education_list": educations,
    }
    return render(request, "education.html", context)

def get_education_json(request):
    educations = Education.objects.all().order_by('-started_year')
    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "form": form,
    }
    return render(request, "education_form.html", context)

def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "form": form,
        "education": education,
    }
    return render(request, "education_form.html", context)


def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

# Projects Section

@login_required(login_url="/login/")
def create_project(request):

    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    is_editor = request.user.groups.filter(name="Editor").exists()
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied

    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "form": form,
        "project": project,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)
    is_editor = request.user.is_authenticated and request.user.groups.filter(name="Editor").exists()

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "project_list": projects,
        "title_query": title_query,
        "is_editor": is_editor,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_project(request, project_id):

    if not request.user.is_superuser:
            raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
        "nickname": "Putra",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")