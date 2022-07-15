import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from apps.index.models import WebUrls
from Arkham import settings

#首页访问
#LoginRequiredMixin用来校验是否登录，没有登陆都跳转登录页
class IndexView(LoginRequiredMixin,View):
    def get(self,request):
        if request.session is not None:
            try:
                #从session中获取当前登录的用户
                loginuser = request.session['user_id']
                context = {
                    'user':loginuser
                }
                #将当前用户名发送到index页面
                return render(request,'index.html',context=context)
            except:
                return redirect(reverse('login'))


#子域名管理

class WebUrlView(LoginRequiredMixin,View):
    redirect_field_name = 'redirect_to'
    def get(self,request):
        a = WebUrls(urid=1,urls='www.baidu.com',state=True)
        a.save()
        return HttpResponse('ok')

    def post(self,request):
        urls = json.loads(request.body)
        for i,j in urls.items():
            print(j)
        return HttpResponse('ok')