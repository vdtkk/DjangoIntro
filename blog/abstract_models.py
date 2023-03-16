from django.db  import models

class DateAbstractModel(models.Model):

    olusturulma_Tarihi=models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi=models.DateTimeField(auto_now=True)   

    class Meta:
      abstract=True


    