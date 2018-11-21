from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from upload.models import Shop


class UploadView(View):

    def get(self,request):
        return render(request,'upload.html')

    def post(self,request):
        # 获取文字字符串部分信息
        desc = request.POST.get('desc')
        name = request.POST.get('name')
        # 获取文件部分信息
        img = request.FILES.get('img')
        # request.FILES.getlist('img')
        shop = Shop(desc=desc,name=name,img=img)
        shop.save()
        return HttpResponse(f"<img src='http://127.0.0.1:8000/media/{shop.img}'width='500'>")

