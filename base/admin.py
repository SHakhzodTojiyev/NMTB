from django.contrib import admin
from .models import (Elonlar, Rahbariyat, Xodimlar, Tadbirlar)
# Register your models here.

 
admin.site.register(Rahbariyat)
admin.site.register(Xodimlar)
admin.site.register(Tadbirlar)
admin.site.register(Elonlar)