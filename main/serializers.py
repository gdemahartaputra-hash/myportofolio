from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Project


def clean_text(value, *, required_message=None):
    value = strip_tags(value).strip()
    if required_message and not value:
        raise serializers.ValidationError(required_message)
    return value


class StarInfoMixin(serializers.Serializer):

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
