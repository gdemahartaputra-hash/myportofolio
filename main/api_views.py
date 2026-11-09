"""API view DRF berbasis fungsi untuk Projects (Tutorial 07) dan Experience (Tugas 6).

Alur setiap request: SessionAuthentication -> permission class -> pemeriksaan
method (@api_view) -> isi view -> serializer -> Response. Validasi ada di
main/serializers.py dan hak akses di main/permissions.py, bukan di sini.
"""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Experience, Project
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import ExperienceSerializer, ProjectSerializer


def toggle_star(instance, user):
    """Memberi star jika `user` belum memberi star, atau membatalkannya jika sudah.

    Akun selalu berasal dari request.user di view, sehingga klien tidak dapat
    memberi star atas nama pengguna lain.
    """
    if instance.starred_by.filter(pk=user.pk).exists():
        instance.starred_by.remove(user)
    else:
        instance.starred_by.add(user)


# Projects API (Tutorial 07)

@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def project_list(request):
    """GET: daftar Project publik (filter ?title=). POST: tambah (pemilik)."""
    if request.method in ("GET", "HEAD"):
        projects = Project.objects.prefetch_related("starred_by").order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            projects = projects.filter(title__icontains=title)
        serializer = ProjectSerializer(
            projects, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = ProjectSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def project_detail(request, project_id):
    """GET: detail publik. PUT/PATCH: ubah (pemilik/Editor). DELETE: hapus (pemilik), 204."""
    project = get_object_or_404(
        Project.objects.prefetch_related("starred_by"), pk=project_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = ProjectSerializer(project, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ProjectSerializer(
        project, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def project_star(request, project_id):
    """POST: toggle star untuk akun yang login, mengembalikan data Project terbaru."""
    project = get_object_or_404(Project, pk=project_id)
    toggle_star(project, request.user)
    serializer = ProjectSerializer(project, context={"request": request})
    return Response(serializer.data)

@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_list(request):
    """GET: daftar Experience publik (filter ?title= dan ?category=). POST: tambah (pemilik)."""
    if request.method in ("GET", "HEAD"):
        experiences = Experience.objects.prefetch_related("starred_by").order_by("-started_at", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            experiences = experiences.filter(title__icontains=title)
        category = request.query_params.get("category", "").strip()
        if category:
            experiences = experiences.filter(category=category)
        serializer = ExperienceSerializer(
            experiences, many=True, context={"request": request},
        )
        return Response(serializer.data)


    serializer = ExperienceSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_detail(request, experience_id):
    """GET: detail publik. PUT/PATCH: ubah (pemilik/Editor). DELETE: hapus (pemilik), 204."""
    experience = get_object_or_404(
        Experience.objects.prefetch_related("starred_by"), pk=experience_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = ExperienceSerializer(experience, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ExperienceSerializer(
        experience, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def experience_star(request, experience_id):
    """POST: toggle star untuk akun yang login, mengembalikan data Experience terbaru."""
    experience = get_object_or_404(Experience, pk=experience_id)
    toggle_star(experience, request.user)
    serializer = ExperienceSerializer(experience, context={"request": request})
    return Response(serializer.data)
