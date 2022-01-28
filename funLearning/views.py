from django.views.generic import TemplateView
from django.apps import apps
from django.shortcuts import redirect, reverse
from teachers.models import User

class HomePageView(TemplateView):
    template_name = 'home_page.html'

def UserHomeView(request):
    if request.user.is_teacher:
        return redirect(reverse("teachers:user_home"))
    else:
        return redirect(reverse("students:user_home"))

class AboutPageView(TemplateView):
    template_name = 'about_page.html'