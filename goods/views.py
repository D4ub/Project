from django.shortcuts import render
from django.template import context


def catalog(request):
    context: dict[str, str] = {
        "title": "Каталог товаров",
        "goods": [
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-5h7-9-11-13-sm-4-sht-27378-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-5h7-9-11-13-sm-4-sht-27382-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
            {
                "image": "deps\img\svechi\komplekt-krasnyh-svechey-bispol-tsilindr-4h6-sm-4-sht-27366-1-660x660.jpg",
                "name": "Комплект цилиндрических свечей Bispol",
                "description": "Комплект цилиндрических свечей Bispol",
                "price": 400,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
