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


#子域名管理接口
class WebUrlView(LoginRequiredMixin,View):
    def post(self,request):
        urls = json.loads(request.body)
        #成功添加的url
        addurls = []
        #错误的url
        errorurls = []
        #重复的url
        checkurls = []
        #判断输入的子域名是否符合格式
        for i, j in urls.items():
            if j.isspace():
                pass
            else:
                #校验子域名格式
                if re.match(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?',j):
                    try:
                        # 校验子域名是否重复
                        a = WebUrls.objects.get(urls=j)
                        #记录重复的域名
                        checkurls.append(j)
                        pass
                    except:
                        urlsave(j)
                        #记录成功添加的域名
                        addurls.append(j)
                else:
                    #记录错误的子域名
                    errorurls.append(j)
        errmsg = '添加成功，成功添加子域名'+str(len(addurls))+'个,错误格式子域名'+str(len(errorurls))+'个,重复子域名'+str(len(checkurls))+'个。'
        return http.JsonResponse({'code': 200, 'errmsg': errmsg,'addurls':addurls,'errorurls':errorurls,'checkurls':checkurls})

#将子域名保存到数据库
def urlsave(urls):
    urlslist = []
    try:
        #取id的最大值然后新增时+1达到自增加的需求
        urlsdata = WebUrls.objects.all()
        for i in urlsdata:
            urlslist.append(i.urid)
        max_data = max(urlslist)
        urlsdemo = WebUrls(urid=max_data+1,urls=urls)
    except:
        urlsdemo = WebUrls(urid=1,urls=urls)
    urlsdemo.save()
