from django.shortcuts import render, redirect
from django.http import HttpResponse

from blog.forms import Iletisimform
from blog.models import iletisimModel

def iletisim(request):
    form=Iletisimform ()
    if request.method=='POST':
      
        form= Iletisimform(request.POST)
        if form.is_valid():
            # print(form.cleaned_data.get('email'))

           iletisim=iletisimModel()
           iletisim.email=form.cleaned_data['email']
           iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
           iletisim.mesaj=form.cleaned_data['mesaj']
           iletisim.save() 
           return redirect('anasayfa')

        else:
            print('valid değil')
    contex = {
       'form': form

    }

    return render(request, 'pages/iletisim.html',context=contex)