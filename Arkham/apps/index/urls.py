from django.urls import path

from apps.index.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    # path('login/', LoginView.as_view()),
]