from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, CharField
from django.forms import forms
from . import models

class TeacherSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_teacher'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_teacher')
        model = get_user_model()

        labels = {
            'first_name':'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email ID',
            'password2': 'Confirm Password',
            'is_teacher': 'Confirm your details please!',
            }
            

        def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
            return user


class CourseCreateForm(ModelForm):

    class Meta:
        fields = ('teacher', 'course_name',)
        model = models.TeacherCourse
        labels = {
            'teacher': 'Course Created By',
            'course_name': 'Course Name'
            }

class CourseQuizForm(ModelForm):

    class Meta:
        fields = ('course', 'quiz_name', 'desc', 'number_of_questions', 'time')
        model = models.Quiz
        labels = {
            'course': 'Course',
            'quiz_name': 'Quiz Name',
            'desc': 'Quiz Description',
            'number_of_questions': 'Number of Questions',
            'time': 'Time Alloted'
            }

class QuesAddForm(ModelForm):

    class Meta:
        fields = ('quiz', 'ques')
        model = models.Question
        labels = {
            'quiz': 'Quiz Name',
            'ques': 'Question'
            }