from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context: dict[str, str] = {
        "title": "Butterfly Decor",
        'categories': categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    context: dict[str, str] = {
        "title": "About",
    }

    return render(request, "main/about.html", context)


def svechi(request):
    context: dict[str, str] = {
        "title": "Svechi",
    }

    return render(request, "main/svechi.html", context)


def fotoramki(request):
    context: dict[str, str] = {
        "title": "Fotoramki",
    }

    return render(request, "main/fotoramki.html", context)


def oplataidostavka(request):
    context: dict[str, str] = {
        "title": "Oplataidostavka",
    }

    return render(request, "main/oplataidostavka.html", context)


def kontaktu(request):
    context: dict[str, str] = {
        "title": "Kontaktu",
    }

    return render(request, "main/kontaktu.html", context)
