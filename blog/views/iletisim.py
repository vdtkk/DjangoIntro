from django.shortcuts import render
from django.http import HttpResponse

def iletisim(request):
 
 contex = {
    'isim': 'VEDAT KIVRAK'

 }

 return render(request, 'pages/iletisim.html',context={})