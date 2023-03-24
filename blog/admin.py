from django.contrib import admin
from blog.models import (KategoriModel 
                         ,YazilarModel,YorumModel,iletisimModel)



admin.site.register(KategoriModel)


@admin.register(YazilarModel)
class yazilarAdmin(admin.ModelAdmin):
    
    search_fields=('baslik','icerik') #searhC ekledik
    list_display=(
        'baslik','olusturulma_Tarihi','duzenlenme_tarihi' #olustuma tarihi ekledik
    )


@admin.register(YorumModel)

class YorumAdmin(admin.ModelAdmin):
    list_display=('yazan','olusturulma_Tarihi','duzenlenme_tarihi')
    search_fields=('yazan__username',)


@admin.register(iletisimModel)

class iletisimAdmin(admin.ModelAdmin):
    list_display=('email','olusturma_Tarihi')
    search_fields=('email',)

