from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.education = Education.objects.create(
            school_name="Universitas Indonesia",
            major="Information System Undergraduate, Faculty of Computer Science",
            grade="Current GPA: 3.82/4.0",
            category="bachelor-degree",
            started_year=2025,
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        # Data dimuat lewat fetch(), jadi HTML hanya berisi kerangka dan alamat endpoint.
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("main:get_experience_json"))
        self.assertNotContains(response, self.experience.title)

    def test_experience_json_returns_data(self):
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.status_code, 200)
        item = response.json()[0]
        fields = item["fields"]
        self.assertEqual(item["pk"], str(self.experience.id))
        self.assertEqual(fields["title"], self.experience.title)
        self.assertEqual(fields["description"], self.experience.description)
        self.assertEqual(fields["category_display"], "Part-Time")
        self.assertTrue(fields["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(self.client.get(reverse("main:get_experience_json")).json(), [])
        self.assertContains(response, 'id="empty"')
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan atau ditemukan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(response.json()[0]["fields"]["is_ongoing"])

    # Education Test

    def test_education_url_is_accessible(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, 'id="grid"')

    def test_education_json_returns_data(self):
        response = self.client.get(reverse("main:get_education_json"))

        self.assertEqual(response.status_code, 200)
        item = response.json()[0]
        fields = item["fields"]
        self.assertEqual(item["pk"], str(self.education.id))
        self.assertEqual(fields["school_name"], self.education.school_name)
        self.assertEqual(fields["major"], self.education.major)
        self.assertEqual(fields["grade"], self.education.grade)
        self.assertEqual(fields["started_year"], 2025)
        self.assertIsNone(fields["ended_year"])
        self.assertTrue(fields["is_ongoing"])

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(self.client.get(reverse("main:get_education_json")).json(), [])
        self.assertContains(response, 'id="empty"')
        self.assertContains(response, "Belum ada riwayat pendidikan yang ditambahkan atau ditemukan.")
