from django.urls import path

from apps.index.views import IndexView,WebUrlView,seturlView


urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('addurls/', WebUrlView.as_view()),
    path('seturls/',seturlView.as_view()),
    # path('login/', LoginView.as_view()),
]