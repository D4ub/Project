from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("svechi/", views.svechi, name="svechi"),
    path("fotoramki/", views.fotoramki, name="fotoramki"),
    path("oplataidostavka/", views.oplataidostavka, name="oplataidostavka"),
    path("kontaktu/", views.kontaktu, name="kontaktu"),
    path("vasu/", views.about, name="vasu"),
    path("korzinu/", views.about, name="korzinu"),
    path("aromadiffuzoru/", views.about, name="aromadiffuzoru"),
    path("bokalu/", views.about, name="bokalu"),
    path("tarelki/", views.about, name="tarelki"),
    path("chashki/", views.about, name="chashki"),
    path("naboruchashek/", views.about, name="naboruchashek"),
    path("sacharnizu/", views.about, name="sacharnizu"),
    path("medovnizu/", views.about, name="medovnizu"),
    path("naborudljspezii/", views.about, name="naborudljspezii"),
    path("zvetu/", views.about, name="zvetu"),
    path("buketu/", views.about, name="buketu"),
    path("odinochnuezvetu/", views.about, name="odinochnuezvetu"),
    path("golovkizvetov/", views.about, name="golovkizvetov"),
    path("minibuketu/", views.about, name="minibuketu"),
    path("zelenidbavki/", views.about, name="zelenidbavki"),
    path("vetkizeleni/", views.about, name="vetkizeleni"),
    path("listiki/", views.about, name="listiki"),
    path("yagodu/", views.about, name="yagodu"),
    path("tuchinki/", views.about, name="tuchinki"),
    path("suchozvetu/", views.about, name="suchozvetu"),
    path("dlyatvorchestva/", views.about, name="dlyatvorchestva"),
    path("floristika/", views.about, name="floristika"),
    path("skrapbuking/", views.about, name="skrapbuking"),
    path("felting/", views.about, name="felting"),
    path("zagotovki/", views.about, name="zagotovki"),
    path("lentu/", views.about, name="lentu"),
    path("businu/", views.about, name="businu"),
    path("fetr/", views.about, name="fetr"),
    path("drugoe/", views.about, name="drugoe"),
    path("melkiydekor/", views.about, name="melkiydekor"),
    path("lipuchli/", views.about, name="lipuchli"),
    path("prishepki/", views.about, name="prishepki"),
    path("babochki/", views.about, name="babochki"),
    path("fruktu/", views.about, name="fruktu"),
    path("rotangovueshariki/", views.about, name="rotangovueshariki"),
    path("drugoedekor/", views.about, name="drugoedekor"),
    path("korobkipaketu/", views.about, name="korobkipaketu"),
    path("detskie/", views.about, name="detskie"),
    path("genskie/", views.about, name="genskie"),
    path("mugskie/", views.about, name="mugskie"),
    path("navupisku/", views.about, name="navupisku"),
    path("posuda/", views.about, name="posuda"),
    path("rasnoe/", views.about, name="rasnoe"),
    path("perja/", views.about, name="perja"),
    path("sharu/", views.about, name="sharu"),
]
