from django.conf.urls import url
from django.contrib.auth import views as auth_views
from students import views

app_name = 'students'

urlpatterns = [
    url(r'^home/', views.HomePageView.as_view(), name='home_page'),
    url(r'^about/', views.AboutPageView.as_view(), name='about'),
    url(r'^$', views.SignupOrLoginView.as_view(), name='signup_or_login'),
    url(r'^user-home/$', views.UserHomeView.as_view(), name='user_home'),
    url(r'^signup/$', views.StudentSignupView.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='students/login.html', extra_context={'next': 'students/user-home'}), name='login'),
    url(r'^profile/$', views.StudentProfileView.as_view(), name='profile'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    ]

