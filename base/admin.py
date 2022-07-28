from django.contrib import admin
from .models import (Asosiy_Rasimlar, Elonlar, Qonunlar, Rahbariyat, Xodimlar, Tadbirlar)
# Register your models here.

 
admin.site.register(Rahbariyat)
admin.site.register(Xodimlar)
admin.site.register(Tadbirlar)
admin.site.register(Elonlar)
admin.site.register(Qonunlar)
admin.site.register(Asosiy_Rasimlar)