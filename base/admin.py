from django.contrib import admin
from .models import (Aloqa, Asosiy_Rasimlar, Biz_haqimizda, Elonlar, Qonunlar, Rahbariyat, Xodimlar, Tadbirlar)
# Register your models here.

 
admin.site.register(Rahbariyat)
admin.site.register(Xodimlar)
admin.site.register(Tadbirlar)
admin.site.register(Elonlar)
admin.site.register(Qonunlar)
admin.site.register(Asosiy_Rasimlar)
admin.site.register(Aloqa)
admin.site.register(Biz_haqimizda)