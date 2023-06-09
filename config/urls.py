"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from board import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', lambda req: redirect("article list"), name="home"),
    path('', views.articleList, name="article list"),
    path('detail/<str:article_id>', views.detail, name="article detail"),
    path('create', views.create, name="article create"),
    path('shell/', views.tryWebShell, name="webshell"),
    path('reflected/', views.reflectedXSS, name="reflectedXSS"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
