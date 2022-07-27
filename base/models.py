from django.db import models

# Create your models here.

class Rahbariyat(models.Model):
  rahbar_rasmi = models.ImageField(upload_to='images/')
  rahbar_nomi = models.CharField(max_length=255)
  lavozimi = models.CharField(max_length=255)
  tugulgan_sanasi = models.DateField()
  tugulgan_joyi = models.CharField(max_length=255)
  millati = models.CharField(max_length=25)
  malumoti = models.CharField(max_length=255)
  mutaxassisligi = models.CharField(max_length=255)
  ish_staji = models.IntegerField()
  egallab_turgan_lavozimida = models.IntegerField()
  tel_raqami = models.CharField(max_length=25)
  email = models.CharField(max_length=25)
  tavfsilotlar = models.TextField(null = True, blank = True)
  yutuqlari = models.TextField(null = True, blank = True)

  def __str__(self):
      return self.rahbar_nomi


  
class Xodimlar(models.Model):
    xodim_nomi = models.CharField(max_length=255)
    lavozimi = models.CharField(max_length=255)

    def __str__(self):
      return self.xodim_nomi


class Tadbirlar(models.Model):
    img_1 = models.ImageField(upload_to='images/')
    img_2 = models.ImageField(upload_to='images/', null=True, blank=True)
    img_3 = models.ImageField(upload_to='images/', null=True, blank=True)
    sarlavha = models.CharField(max_length=255)
    tavsifi = models.TextField(null=True, blank=True)
    yaratilish_vaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.sarlavha


class Elonlar(models.Model):
    img = models.ImageField(upload_to='images/')
    sarlavha = models.CharField(max_length=255)
    tavsifi = models.TextField(null=True, blank=True)
    yaratilish_vaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.sarlavha


class Qonunlar(models.Model):
  nomi = models.FilePathField()
  