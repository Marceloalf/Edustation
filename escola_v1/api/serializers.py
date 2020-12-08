from rest_framework_simplejwt.views import TokenObtainPairView

from escola_v1.models import *

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings


class StudentSerializer(serializers.ModelSerializer):
    classes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='classes-detail',
    )

    class Meta:
        model = Students
        fields = (
            'id',
            'name',
            'cpf',
            'birth',
            'email',
            'user',
            'classes'
        )


class TeacherSerializer(serializers.ModelSerializer):
    classes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='classes-detail',
    )

    class Meta:
        model = Teachers
        fields = (
            'id',
            'name',
            'cpf',
            'birth',
            'email',
            'user',
            'classes'
        )


class SubjectSerializer(serializers.ModelSerializer):
    classes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='classes-detail',
    )

    class Meta:
        model = Subjects
        fields = (
            'id',
            'name',
            'created_at',
            'classes'
        )


class ClassesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"


class UserSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['id'] = self.user.id
        data['access exp'] = api_settings.__getattr__('ACCESS_TOKEN_LIFETIME')
        data['refresh exp'] = api_settings.__getattr__('REFRESH_TOKEN_LIFETIME')

        return data


class JoinClassesSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    class_ = serializers.PrimaryKeyRelatedField(queryset=Classes.objects)
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teachers.objects, allow_null=True)
    student = serializers.PrimaryKeyRelatedField(queryset=Students.objects, allow_null=True)
    subject = serializers.PrimaryKeyRelatedField(queryset=Subjects.objects, allow_null=True)

    def create(self, validated_data):
        if validated_data['class'] is not None:
            class_ = validated_data['class']

        if validated_data['student'] is not None:
            student = validated_data['student']
            class_.add(student)

        if validated_data['teacher'] is not None:
            teacher = validated_data['teacher']
            class_.add(teacher)

        if validated_data['subject'] is not None:
            subject = validated_data['subject']
            class_.add(subject)
