"""
funLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePageView.as_view(), name='home_page'),
    url(r'^about/', views.AboutPageView.as_view(), name='about'),
    url(r'^teachers/', include('teachers.urls', namespace='teachers')),
    url(r'^teachers/', include('django.contrib.auth.urls')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^students/', include('django.contrib.auth.urls')),
    url(r'^user-home/', views.UserHomeView, name='user_home'),
]