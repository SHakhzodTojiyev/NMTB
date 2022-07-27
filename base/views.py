from django.shortcuts import render
from .models import (Rahbariyat, Xodimlar, Tadbirlar, Elonlar)

# Create your views here.
def home(request):
  return render(request, 'pages/home.html')

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
  return render(request, 'pages/qonunlar.html')


def aloqa(request):
  return render(request, 'pages/contact.html')