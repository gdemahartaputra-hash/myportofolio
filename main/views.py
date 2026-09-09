from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Gde Maharta Putra Wicaksana Ridjasa",
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
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)