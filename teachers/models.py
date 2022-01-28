from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.conf import settings

class User(auth.models.AbstractUser):
    is_student = models.BooleanField('Student Status', default=False, null=False)
    is_teacher = models.BooleanField('Teacher Status', default=False, null=False)

    def __str__(self):
        return self.username

class TeacherCourse(models.Model):
    course_name = models.CharField(max_length=256, null=False)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, help_text="Select your 'username'!", related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('teachers:course_list')

class Quiz(models.Model):
    course = models.OneToOneField(TeacherCourse, help_text="Select any course created by you!", related_name="quiz", on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=256, null=False)
    desc = models.TextField()  
    number_of_questions = models.IntegerField(null=False)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", null=False)
    
    def __str__(self):
        return self.quiz_name

    def get_questions(self):
        return self.question_set.all()

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="question", help_text="Select the same quiz whose questions you are viewing!", on_delete=models.CASCADE)
    ques = models.TextField()
    
    def __str__(self):
        return self.ques
    
    def get_answers(self):
        return self.answer_set.all() 

#class Answer(models.Model):
#    question = models.ForeignKey(Question, related_name ="answers", on_delete=models.CASCADE)
#    content = models.TextField()
#    correct = models.BooleanField(default=False)
    
#    def __str__(self):
#        return f"Question: {self.question.content}, Answer: {self.content}, Correct: {self.correct}" 

##class Marks_Of_Student(models.Model):
##    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
##    user = models.ForeignKey(User, on_delete=models.CASCADE)
##    score = models.FloatField()
    
##    def __str__(self):
##        return str(self.quiz)