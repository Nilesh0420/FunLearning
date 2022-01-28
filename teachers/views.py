from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from . import forms, models

class SignupOrLoginView(TemplateView):
    template_name = 'teachers/signup_or_login.html'

class UserHomeView(TemplateView):
    template_name = 'teachers/user_home.html'

class TeacherProfileView(TemplateView):
    template_name = 'teachers/profile.html'

class HomePageView(TemplateView):
    template_name = 'teachers/home_page.html'

class AboutPageView(TemplateView):
    template_name = 'teachers/about_page.html'

class TeacherSignupView(CreateView):
    form_class = forms.TeacherSignupForm
    template_name = 'teachers/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect(reverse_lazy('teachers:login'))

class CourseListView(ListView):
    model = models.TeacherCourse   
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = models.TeacherCourse
    template_name = 'teachers/teachercourse_detail.html'
    context_object_name = 'course_details'

class CourseCreateView(CreateView):
    form_class = forms.CourseCreateForm
    template_name = 'teachers/teachercourse_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect(reverse_lazy('teachers:course_list'))

class CourseUpdateView(UpdateView):
    fields = ('teacher', 'course_name')
    model = models.TeacherCourse
    success_url = reverse_lazy("teachers:course_list")

class CourseDeleteView(DeleteView):
    model = models.TeacherCourse
    success_url = reverse_lazy("teachers:course_list")
    context_object_name = 'course'

class CourseQuizView(CreateView):
    form_class = forms.CourseQuizForm
    template_name = 'teachers/quiz_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect(reverse_lazy('teachers:quiz_list'))

class QuizListView(ListView):
    model = models.Quiz   
    context_object_name = 'quizes'

class QuizDetailView(DetailView):
    model = models.Quiz
    template_name = 'teachers/quiz_detail.html'
    context_object_name = 'quiz_details'

class QuesListView(ListView):
    model = models.Question
    context_object_name = 'questions'

class QuesAddView(CreateView):
    form_class = forms.QuesAddForm
    template_name = 'teachers/question_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect(reverse_lazy('teachers:ques_list'))

class QuesDetailView(DetailView):
    model = models.Question
    template_name = 'teachers/question_detail.html'
    context_object_name = 'ques_details'

class QuesUpdateView(UpdateView):
    fields = ('quiz', 'ques')
    model = models.Question
    success_url = reverse_lazy("teachers:ques_list")

class QuesDeleteView(DeleteView):
    model = models.Question
    success_url = reverse_lazy("teachers:ques_list")
    context_object_name = 'ques'