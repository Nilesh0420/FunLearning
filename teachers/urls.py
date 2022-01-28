from django.conf.urls import url
from django.contrib.auth import views as auth_views
from teachers import views

app_name = 'teachers'

urlpatterns = [
    url(r'^home/', views.HomePageView.as_view(), name='home_page'),
    url(r'^about/', views.AboutPageView.as_view(), name='about'),
    url(r'^$', views.SignupOrLoginView.as_view(), name='signup_or_login'),
    url(r'^user-home/$', views.UserHomeView.as_view(), name='user_home'),
    url(r'^signup/$', views.TeacherSignupView.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='teachers/login.html', extra_context={'next': 'teachers/user-home'}), name='login'),
    url(r'^profile/$', views.TeacherProfileView.as_view(), name='profile'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^user-home/courses/', views.CourseListView.as_view(), name='course_list'),
    url(r'^user-home/view-course/(?P<pk>\d+)/', views.CourseDetailView.as_view(), name='course_detail'),
    url(r'^user-home/add-course/$', views.CourseCreateView.as_view(), name='course_create'),
    url(r'^user-home/update-course/(?P<pk>\d+)/', views.CourseUpdateView.as_view(), name='course_update'),
    url(r'^user-home/delete-course/(?P<pk>\d+)/', views.CourseDeleteView.as_view(), name='course_delete'),
    url(r'^user-home/create-quiz/', views.CourseQuizView.as_view(), name='course_quiz'),
    url(r'^user-home/quizes/', views.QuizListView.as_view(), name='quiz_list'),
    url(r'^user-home/quiz-details/(?P<pk>\d+)/', views.QuizDetailView.as_view(), name='quiz_detail'),
    url(r'^user-home/quiz/questions/', views.QuesListView.as_view(), name='ques_list'),
    url(r'^user-home/my-quiz/add-ques/', views.QuesAddView.as_view(), name='ques_add'),
    url(r'^user-home/ques-details/(?P<pk>\d+)/', views.QuesDetailView.as_view(), name='ques_detail'),
    url(r'^user-home/update-ques/(?P<pk>\d+)/', views.QuesUpdateView.as_view(), name='ques_update'),
    url(r'^user-home/delete-ques/(?P<pk>\d+)/', views.QuesDeleteView.as_view(), name='ques_delete'),
    ]

