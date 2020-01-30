from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.pagPrincipal),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]