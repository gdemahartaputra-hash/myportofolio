"""Serializer DRF untuk API portofolio (/api/v1/).

Serializer bertanggung jawab atas dua arah data: mengubah objek model menjadi
representasi JSON (serialization) dan memvalidasi input klien sebelum disimpan
(deserialization). Hak akses tidak diatur di sini, melainkan di main/permissions.py.
"""

from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Project


def clean_text(value, *, required_message=None):
    """Membuang tag HTML dan spasi di tepi teks.

    Jika `required_message` diisi dan hasil pembersihan kosong (misalnya input
    hanya berisi tag seperti "<b></b>"), input ditolak dengan pesan tersebut.
    strip_tags bukan sanitizer HTML; frontend tetap wajib melakukan escaping.
    """
    value = strip_tags(value).strip()
    if required_message and not value:
        raise serializers.ValidationError(required_message)
    return value


class StarInfoMixin(serializers.Serializer):
    """Field star read-only yang dipakai bersama oleh Project dan Experience.

    Membutuhkan model dengan relasi ManyToMany `starred_by` ke User dan
    `request` di context serializer agar `is_starred` sesuai akun yang login.
    Ketiga method membaca `starred_by.all()`/`.count()`, sehingga jika queryset
    memakai prefetch_related("starred_by"), tidak ada query tambahan per objek.
    Hanya username yang diekspos; email dan data akun lain tidak ikut tampil.
    """

    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())


class ProjectSerializer(StarInfoMixin, serializers.ModelSerializer):
    """Representasi dan validasi Project untuk API /api/v1/projects/ (Tutorial 07)."""

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        return clean_text(value, required_message="Title cannot be empty.")

    def validate_description(self, value):
        return clean_text(value)

    def validate_tech_stack(self, value):
        return clean_text(value)


class ExperienceSerializer(StarInfoMixin, serializers.ModelSerializer):
    """Representasi dan validasi Experience untuk API /api/v1/experience/ (Tugas 6).

    `category` ditulis sebagai kunci pilihan (misalnya "part-time"), sedangkan
    `category_display` adalah label yang siap ditampilkan ("Part-Time").
    `started_at` diisi otomatis oleh model (auto_now_add) sehingga read-only.
    """

    category_display = serializers.CharField(source="get_category_display", read_only=True)
    is_ongoing = serializers.BooleanField(read_only=True)

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category", "category_display",
            "thumbnail", "started_at", "ended_at", "is_ongoing",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id", "started_at"]

    def validate_title(self, value):
        return clean_text(
            value,
            required_message="Judul pengalaman tidak boleh kosong atau hanya berisi tag HTML.",
        )

    def validate_description(self, value):
        return clean_text(
            value,
            required_message="Deskripsi tidak boleh kosong atau hanya berisi tag HTML.",
        )
