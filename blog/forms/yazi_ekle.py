from django import forms
from blog.models import YazilarModel

# yazılar modelindeki modeli class da kullancağımız içib 
#oradaki fieldlara ulaşmak içib blog.model den yazıalr modeli ekliyoruz
#devamında fieldlarını çağırmak için exclude diyerek sadece istemediğimiz fieldları yazıyoruz
#ki 2 tane istemediğimiz lar sırf 2 tane için hepsini yazmayalım. 


class YazıEkleModelForm(forms.ModelForm):
     class Meta:
        
          model=YazilarModel

          exclude=('yazar','slug')