from django.urls import path, include

from rest_framework.routers import DefaultRouter
from escola_v1.views import *


router = DefaultRouter()
router.register(r'class', ClassesViewSet)
router.register(r'join', JoinViewSet, basename='join')

instance_router = DefaultRouter()
instance_router.register(r'student', StudentsViewSet)
instance_router.register(r'teacher', TeacherViewSet)
instance_router.register(r'subject', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls), name='router_urls'),
    path('', include(instance_router.urls), name='router_urls'),
    path('class/<int:classes_pk>/', include(instance_router.urls)),
    path('login', UserViewSet.as_view()),
]
