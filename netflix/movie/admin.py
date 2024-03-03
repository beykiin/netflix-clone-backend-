from django.contrib import admin
from .models import *
# from .models import YourModel

# admin.site.register(YourModel)
class MoviesAdmin(admin.ModelAdmin):
    list_display=["id","isim","kategori"] #Admin sayfasında gözükecek listeleme şekli
    list_display_links=["isim"]  #Admin sayfasında link olan kısmı değiştiriyor id den isme geçti
    list_editable=["kategori"] #Liste gösterilirken düzenlenebilir yapmak için kullanılıyr
    list_filter=["kategori"] #filtreleme yapmak için kullanılıyor
    list_per_page=2 #Sayfaları bölüyor ve bir sayfada sadece iki içerik gözüküyor
# Register your models here.
admin.site.register(Movies,MoviesAdmin)
admin.site.register(Kategoriler)
admin.site.register(Tur)
admin.site.register(Izlenenler)


# change_forms_template araştır