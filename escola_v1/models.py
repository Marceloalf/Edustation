from django.db import models
from .s_year import school_years


class BaseUser(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    birth = models.DateField()
    email = models.EmailField(unique=True)


class Students(BaseUser):
    user = 'Student'


class Teachers(BaseUser):
    user = 'Teacher'


class Subjects(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Classes(models.Model):
    sy = school_years()
    name = models.CharField(max_length=10)
    school_year = models.CharField(max_length=18, choices=sy)
    created_at = models.DateTimeField(auto_now_add=True)
    student = models.ManyToManyField(Students, related_name='student_classes', blank=True)
    teachers = models.ManyToManyField(Teachers, related_name='teacher_classes', blank=True)
    subject = models.ManyToManyField(Subjects, related_name='subject_classes', blank=True)

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'
