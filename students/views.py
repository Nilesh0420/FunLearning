from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from . import forms

class SignupOrLoginView(TemplateView):
    template_name = 'students/signup_or_login.html'

class UserHomeView(TemplateView):
    template_name = 'students/user_home.html'

class StudentProfileView(TemplateView):
    template_name = 'students/profile.html'

class HomePageView(TemplateView):
    template_name = 'students/home_page.html'

class AboutPageView(TemplateView):
    template_name = 'students/about_page.html'

class StudentSignupView(CreateView):
    form_class = forms.StudentSignupForm
    template_name = 'students/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect(reverse_lazy('students:login'))