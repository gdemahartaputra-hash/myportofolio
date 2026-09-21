from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput, NumberInput

from main.models import Project, Experience, Education

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={"placeholder": "Software Engineer Intern"}
            ),
            "description": Textarea(
                attrs={"placeholder": "Ceritakan pengalamanmu", "rows": 3}
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"}
            ),
            "ended_at": DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "school_name",
            "major",
            "grade",
            "category",
            "thumbnail",
            "started_year",
            "ended_year",
        ]

        labels = {
            "school_name": "Nama Sekolah/Universitas",
            "major": "Jurusan",
            "grade": "Nilai/IPK",
            "category": "Jenjang",
            "thumbnail": "URL Logo",
            "started_year": "Tahun Mulai",
            "ended_year": "Tahun Selesai",
        }

        widgets = {
            "school_name": TextInput(attrs={"placeholder": "Universitas Indonesia"}),
            "major": TextInput(attrs={"placeholder": "Sistem Informasi"}),
            "grade": TextInput(attrs={"placeholder": "3.90/4.00"}),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"}
            ),
            "started_year": NumberInput(attrs={"placeholder": "2025"}),
            "ended_year": NumberInput(attrs={"placeholder": "2029"}),
        }