from django import forms
from blog.models import iletisimModel

class Iletisimform(forms.ModelForm):
        class Meta:
           model= iletisimModel
           fields=('isim_soyisim','email','mesaj')


# class Iletisimform(forms.Form):
#         email= forms.EmailField(label='E-Posta',max_length=100)
#         isim_soyisim = forms.CharField(label='İsim Soyisim', max_length=10)
#         mesaj=forms.CharField(label='Mesajınız',widget=forms.Textarea)