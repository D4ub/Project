from django.shortcuts import render
from django.template import context

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context: dict[str, str] = {
        "title": "Каталог товаров",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context: dict[str, str] = {
        "product": product
    }
        
     
    return render(request, "goods/product.html", context=context)
