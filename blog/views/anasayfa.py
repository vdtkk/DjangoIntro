from django.shortcuts import render


def anasayfa(request):

 contex = {
    'isim': 'VEDAT KIVRAK anasayfa'

 }

 return render(request, 'pages/anasayfa.html',context={})