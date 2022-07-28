from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),

    path("biz-haqimizda/", views.about, name='about'),

    path("rahbariyat/", views.rahbariyat, name='rahbariyat'),
    
    path("xodimlar/", views.xodimlar, name='xodimlar'),

    path("tadbirlar/", views.tadbirlar, name='tadbirlar'),
    path("tadbir/<int:pk>", views.tadbir, name='tadbir'), 

    path("elonlar/", views.elonlar, name='elonlar'),
    path("elon/<int:pk>", views.elon, name='elon'),

    path("qonunlar/", views.qonunlar, name='qonunlar'),

    path("farmonlar/", views.farmonlar, name='farmonlar'),
    
    path("aloqa/", views.aloqa, name='aloqa'),
]
