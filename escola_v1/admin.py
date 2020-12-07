from django.contrib import admin
from .models import *


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'name',
            'cpf',
            'birth',
            'email',
            'user'
        )


@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'name',
            'cpf',
            'birth',
            'email',
            'user'
        )


@admin.register(Subjects)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'name',
            'created_at'
        )


@admin.register(Classes)
class Classes(admin.ModelAdmin):
    list_display = (
        'name',
        'school_year',
        'created_at'
    )
