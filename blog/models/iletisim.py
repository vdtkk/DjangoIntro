from django.db import models

class iletisimModel(models.Model):

    email=models.EmailField(max_length=250)
    isim_soyisim=models.CharField(max_length=150)
    mesaj=models.TextField()
    olusturma_Tarihi=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='iletisim'
        verbose_name='iletisim'
        verbose_name_plural='iletisim'

    def __str__(self):
        return self.email