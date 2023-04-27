from django.shortcuts import render, redirect
from django.http import HttpResponse

from blog.forms import Iletisimform
from blog.models import iletisimModel

def iletisim(request):
    form=Iletisimform ()


    #---burada data ve initial farkını görüntüledik----
    # #(data={ #initial yazılır ise  form başlangıç değeri anlamına gelir ve aşağıda fieldlar tanımlanır.
    #     'isim_soyisim':'',
    #     'email':'vdtkk@mynet.com.tr',
    #     'mesaj': 'bu bir testtir'
    # })


    if request.method=='POST':
      
        form= Iletisimform(request.POST)
        if form.is_valid():
            # print(form.cleaned_data.get('email'))

        #    iletisim=iletisimModel()
        #    iletisim.email=form.cleaned_data['email']
        #    iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
        #    iletisim.mesaj=form.cleaned_data['mesaj']
        #    iletisim.save() 
           form.save()
           return redirect('anasayfa')

        else:
            print('valid değil')
    contex = {
       'form': form

    }

    return render(request, 'pages/iletisim.html',context=contex)