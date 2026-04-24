"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include #44
from authorization.views import RegisterView #45
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #46

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', RegisterView.as_view(), name='register'), #47
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #48
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #50 -> adımlar.txt
]
