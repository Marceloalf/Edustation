from escola_v1 import models

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings


class StudentSerializer(serializers.ModelSerializer):
    student_classes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='classes-detail',
    )

    class Meta:
        model = models.Students
        fields = (
            'id',
            'name',
            'cpf',
            'birth',
            'email',
            'user',
            'student_classes'
        )


class TeacherSerializer(serializers.ModelSerializer):
    teacher_classes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='classes-detail',
    )

    class Meta:
        model = models.Teachers
        fields = (
            'id',
            'name',
            'cpf',
            'birth',
            'email',
            'user',
            'teacher_classes'
        )


class SubjectSerializer(serializers.ModelSerializer):
    subject_classes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='classes-detail',
    )

    class Meta:
        model = models.Subjects
        fields = (
            'id',
            'name',
            'created_at',
            'subject_classes'
        )


class ClassesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Classes
        fields = "__all__"


class UserSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['id'] = self.user.id
        data['access exp'] = api_settings.__getattr__('ACCESS_TOKEN_LIFETIME')
        data['refresh exp'] = api_settings.__getattr__('REFRESH_TOKEN_LIFETIME')

        return data


class JoinClassesSerializer(serializers.Serializer):
    classes = serializers.PrimaryKeyRelatedField(queryset=models.Classes.objects)
    subject = serializers.PrimaryKeyRelatedField(queryset=models.Subjects.objects, required=False)
    teacher = serializers.PrimaryKeyRelatedField(queryset=models.Teachers.objects, required=False)
    student = serializers.PrimaryKeyRelatedField(queryset=models.Students.objects, required=False)

    def create(self, validated_data):
        classes = validated_data['classes']

        if "subject" in validated_data:
            subject = validated_data['subject']
            classes.subject.add(subject)

        if "teacher" in validated_data:
            teacher = validated_data['teacher']
            classes.teacher.add(teacher)

        if "student" in validated_data:
            student = validated_data['student']
            classes.student.add(student)

        return validated_data
