import json
import re

from django import http
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth import logout
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
# Create your views here.
from django.views import View
from django.core.mail import send_mail
from calery_tasks.sendMail.tasks import send_Email

from apps.users.models import User

# 用户登录功能
class LoginView(View):
    """
    1、用户首次登录时，按照默认的用户名密码进行数据库创建并且保持登录状态。
    2、用户登录后，通过session保持用户权限，并且将用户名与session绑定方便后续用户权限校验。
    3、
    """
    def get(self, request):
        if request.session is not None:
            try:
                #从session中获取当前登录的用户
                loginuser = request.session['user_id']
                context = {
                    'user':loginuser
                }
                #将当前用户名发送到index页面
                return redirect(reverse('index'))
            except:
                return render(request, 'login.html')

    def post(self, request):
        # 接收用户提交的数据
        postData = json.loads(request.body)
        username = postData.get('username')
        password = postData.get('password')
        # 判断用户是否合法
        if not re.match(r'[0-9a-zA-Z]{5,20}', username):
            return http.JsonResponse({'code': 500, 'errmsg': '用户名格式错误'})
        # 判断密码是否合法
        if not re.match(r'[0-9a-zA-Z]{5,20}', password):
            # return http.HttpResponseBadRequest('密码格式错误')
            return http.JsonResponse({'code': 500, 'errmsg': '密码格式错误'})
        # 用户认证引用django.contrib.auth中authenticate,验证用户密码是否正确
        authuser = authenticate(username=username, password=password)
        if authuser is not None:
            # 保存
            login(request, authuser)
            # 将登录用户名与session绑定
            request.session['user_id'] = authuser
            # 登陆后跳转首页，reverse需要引入django.urls
            # return redirect(reverse('index'))
            return http.JsonResponse({'code': 200, 'errmsg': '登录成功'})

        # 默认注册admin账户
        elif (username == 'admin' and password == 'Acam123'):
            try:
                user = User.objects.get(username=username)
                # return HttpResponse('用户名或密码错误')
                return http.JsonResponse({'code': 500, 'errmsg': '用户名或密码错误'})
            except Exception as e:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                request.session['user_id'] = user
                return http.JsonResponse({'code': 200, 'errmsg': '登录成功'})
                # return redirect(reverse('index'))
        else:
            return http.JsonResponse({'code': 500, 'errmsg': '用户名或密码错误'})

# 用户退出功能
class LoginOutView(View):
    def get(self, request):
        # 调用django自带的退出功能，执行了request.session.flush()
        logout(request)
        # 退出后进行跳转
        return redirect(reverse('login'))

# 用户信息,实现用户的邮箱验证和修改
class userInfoView(View):
    # 访问用户信息将用户名，邮箱返回
    def get(self, request):
        # 获取登录用户名
        loginuser = request.user
        email = request.user.email
        context = [{
            'loginuser': str(loginuser),
            'loginemail': str(email)
        }]
        context = json.dumps(context)
        return HttpResponse(context)

    # post进行邮箱修改
    # 前端接收传入的邮箱，验证邮箱后存入邮箱绑定当前用户
    def post(self, request):
        # 1、获取邮箱数据
        a = json.loads(request.body)
        data = a.get('email')
        # 2、验证邮箱数据
        if not re.match(r'^[a-zA-Z0-9]+([-_.][A-Za-zd]+)*@([a-zA-Z0-9]+[-.])+[A-Za-zd]{2,5}$', data):
            return http.JsonResponse({'code': 500, 'errmsg': 'email error'})
        else:
            # 3、保存数据,直接引用request.user.email进行保存
            try:
                request.user.email = data
                request.user.save()
            except Exception as e:
                return http.JsonResponse({'code': 500, 'errmsg': 'save error'})
        # 4、发送验证邮件
        # 采用celery异步任务执行邮件的发送操作
        # send_Email.delay(data)
        return http.JsonResponse({'code': 200, 'errmsg': 'email update success!'})

# 修改密码功能
class changepassView(View):
    def post(self, request):
        p = json.loads(request.body)
        oldpass = p.get('oldpass')
        newpass1 = p.get('newpass1')
        newpass2 = p.get('newpass2')
        user = User.objects.get(username=request.user)
        if not re.match(r'[0-9a-zA-Z]{5,20}', oldpass):
            return http.JsonResponse({'code': 201, 'errmsg': '密码格式不正确！'})
        if not re.match(r'[0-9a-zA-Z]{5,20}', newpass1):
            return http.JsonResponse({'code': 201, 'errmsg': '密码格式不正确！'})
        if not re.match(r'[0-9a-zA-Z]{5,20}', newpass2):
            return http.JsonResponse({'code': 201, 'errmsg': '密码格式不正确！'})
        if (newpass1 == newpass2 == oldpass):
            return http.JsonResponse({'code': 202, 'errmsg': '不能和原密码相同！'})
        if user.check_password(oldpass):
            if (newpass1 == newpass2):
                user.set_password(raw_password=newpass1)
                user.save()
                update_session_auth_hash(request, user)
                return http.JsonResponse({'code': 200, 'errmsg': '密码修改成功！'})
        else:
            return http.JsonResponse({'code': 203, 'errmsg': '旧密码不正确！'})
