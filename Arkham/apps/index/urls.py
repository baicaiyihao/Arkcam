from django.urls import path

from apps.index.views import IndexView,WebUrlView


urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('add/', WebUrlView.as_view()),
    # path('login/', LoginView.as_view()),
]