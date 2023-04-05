

from django.urls import path, include
from blog.views import iletisim, anasayfa,kategori,yazilarim,detay
#from django.contrib.auth import view as aut_views  
urlpatterns = [
    #path('giris', aut_views.LoginView.as_view(template_name='pages/giris.html' ), name='giris'),
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim,name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
    ]

