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
