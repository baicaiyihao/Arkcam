from django.urls import path

from apps.tools.views import get_urls_Sylas


urlpatterns = [
    path('get_urls/',get_urls_Sylas.as_view()),
    # path('login/', LoginView.as_view()),
]