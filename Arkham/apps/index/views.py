from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.urls import reverse
from django.views import View


class IndexView(View):
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