from django.contrib import admin
from blog.models import (KategoriModel 
                         ,YazilarModel,YorumModel,iletisimModel)



admin.site.register(KategoriModel)

class yazilarAdmin(admin.ModelAdmin):
    
    search_fields=('baslik','icerik') #searh ekledik
    list_display=(
        'baslik','olusturulma_Tarihi','duzenlenme_tarihi' #olustuma tarihi ekledik
    )

admin.site.register(YazilarModel,yazilarAdmin)

class YorumAdmin(admin.ModelAdmin):
    list_display=('yazan','olusturma_Tarihi','guncellenme_Tarihi')
    search_fields=('yazan__username',)


admin.site.register(YorumModel,YorumAdmin)

class iletisimAdmin(admin.ModelAdmin):
    list_display=('email','olusturma_Tarihi')
    search_fields=('email',)

admin.site.register(iletisimModel,iletisimAdmin)