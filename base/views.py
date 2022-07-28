from django.shortcuts import render
from .models import (Aloqa, Asosiy_Rasimlar, Biz_haqimizda, Rahbariyat, Xodimlar, Tadbirlar, Elonlar, Qonunlar)

# Create your views here.
def home(request):
  asosiy_rasimlar = Asosiy_Rasimlar.objects.all()
  biz_haqimizda = Biz_haqimizda.objects.all()
  context = {
    'asosiy_rasimlar': asosiy_rasimlar, 
    'biz': biz_haqimizda
  }
  return render(request, 'pages/home.html', context)

def about(request):
  return render(request, 'pages/about.html')


def rahbariyat(request):
  rahbar = Rahbariyat.objects.all()
  context = {'rahbar' : rahbar}
  return render(request, 'pages/rahbariyat.html', context)


def xodimlar(request):
  xodim = Xodimlar.objects.all()
  context = {'xodim' : xodim}
  return render(request, 'pages/xodimlar.html', context)


def tadbirlar(request):
    tadbirlar = Tadbirlar.objects.all()
    context = {'tadbir': tadbirlar}
    return render(request, 'pages/tadbirlar.html', context)

def tadbir(request, pk):
    tadbir_haqida = Tadbirlar.objects.get(pk = pk)
    context = {'tadbir_haqida': tadbir_haqida}
    return render(request, 'pages/tadbir.html', context)


def elonlar(request):
  elonlar = Elonlar.objects.all()
  context = {'elon': elonlar}
  return render(request, 'pages/elonlar.html', context)

def elon(request, pk):
  elon_haqida = Elonlar.objects.get(pk = pk)
  context = {'elon_haqida': elon_haqida}
  return render(request, 'pages/elon.html', context)


def qonunlar(request):
  qonun = Qonunlar.objects.order_by("-id").all()
  context = {'qonun': qonun}
  return render(request, 'pages/qonunlar.html', context)


def aloqa(request):
  aloqa = Aloqa.objects.all()
  context = {'aloqa': aloqa}
  return render(request, 'pages/contact.html', context)