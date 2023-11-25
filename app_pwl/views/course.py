from django.db.models import Count
from rest_framework import viewsets

from app_pwl.models import Course
from app_pwl.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(lesson_count=Count('lessons'))
        return queryset
