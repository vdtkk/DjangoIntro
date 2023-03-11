from django import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User

class YazilarModel(models.Model):
    resim=models.ImageField(upload_too='yazi_resimleri')
    baslik=models.CharField(max_length=50)
    icerik=models.TextField()
    olusturulma_Tarihi=models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi=models.DateTimeField(auto_now_add=True)   
    slug=AutoSlugField(populate_from='baslik',unique=True)
    kategoriler= models.ManyToManyField(KategoriModel,related_name='yazi')
    yazar=models.foreignKey(User, on_delete=models.CASCADE,related_name='yazilar')   


    class Meta:
       verbose_name='yazi'
       verbose_name_plural='Yazilar'
       db_name='Yazi'       