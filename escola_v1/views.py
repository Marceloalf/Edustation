from rest_framework import viewsets

from .api.serializers import *


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return self.queryset.filter(classes__pk=self.kwargs.get('classes_pk'))


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return self.queryset.filter(classes__pk=self.kwargs.get('classes_pk'))


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return self.queryset.filter(classes__pk=self.kwargs.get('classes_pk'))


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer


class UserViewSet(TokenObtainPairView):
    serializer_class = UserSerializer
