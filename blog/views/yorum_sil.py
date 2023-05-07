from django.contrib.auth.decorators import login_required
from blog.models import YorumModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url="/")  # dışarıdan kullanıcı girerse anasayfa yönlendirir
def yorum_sil(request, id):
    yorum = get_object_or_404(YorumModel, id=id)
    print(yorum)
    if yorum.yazan == request.user or yorum.yazi.yazar == request.user:
        yorum.delete()
        return redirect("detay", slug=yorum.yazi.slug)

    return redirect("anasayfa")  ## yazılarım linkine göndeririz
