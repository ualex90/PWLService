from django.db.models import Count
from rest_framework import viewsets

from app_pwl.models import Course
from app_pwl.serializers.course import CourseSerializer, CourseListSerializer, CourseRetrieveSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializers = {
        "list": CourseListSerializer,
        "retrieve": CourseRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        # При запросе списка курсов
        # в queryset добавляем поле lesson_count
        # путем подсчета объектов привязанных по ForeignKey
        # по related_name поля course модели Lesson
        self.queryset = self.queryset.annotate(lesson_count=Count('lessons'))
        return super().list(request, *args, **kwargs)
