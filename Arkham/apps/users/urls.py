from django.urls import path
from apps.users import views
from apps.users.views import LoginView, LoginOutView,userInfoView,changepassView

urlpatterns = [
    #url路由跳转，设置别名可以方便后续修改
    path('login/', LoginView.as_view(),name='login'),
    path('loginout/', LoginOutView.as_view(),name='loginout'),
    path('userinfo/', userInfoView.as_view()),
    path('changepass/',changepassView.as_view()),
]