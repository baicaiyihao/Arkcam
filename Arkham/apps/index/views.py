import json
import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.urls import reverse
from django import http
from django.views import View
from apps.index.models import WebUrls
from Arkham import settings
from django.core.paginator import Paginator
from calery_tasks.saveurls.tasks import save_urls

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


#子域名管理添加urls接口
class WebUrlView(LoginRequiredMixin,View):
    def post(self,request):
        body = json.loads(request.body)
        urls = []
        errorurls = []
        #判断输入的子域名是否符合格式
        for i, j in body.items():
            if j.isspace():
                pass
            else:
                #校验子域名格式
                if re.match(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?',j):
                    urls.append(j)
                else:
                    #记录错误的子域名
                    errorurls.append(j)
        return save_urls(urls,errorurls)


#子域名管理查询urls接口
class seturlView(LoginRequiredMixin,View):
    def get(self,request):
        url = []
        j = {}
        id = 0
        a = WebUrls.objects.all()
        #按格式输出所有的子域名
        for i in a:
            id = id+1
            j = {
                'id':str(id),
                'urls':i.urls,
                'code':str(i.statecode),
                'state':str(i.state),
                'jointime':str(i.time),
            }
            url.append(j)
        #利用Paginator分页器进行分页
        limit = request.GET.get('limit')
        page = request.GET.get('page')
        outA = Paginator(url,limit)
        outB = outA.page(page)
        return http.JsonResponse({'code': 0,"msg": "","count": len(url),"data":outB.object_list})
