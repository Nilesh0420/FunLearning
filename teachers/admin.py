from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'password', 'is_teacher', 'is_student')})
UserAdmin.fieldsets = tuple(fields)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.TeacherCourse)
admin.site.register(models.Quiz)
admin.site.register(models.Question)
#admin.site.register(models.Answer)
