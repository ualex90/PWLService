from django.db.models import Count
from rest_framework import viewsets

from app_pwl.models import Course
from app_pwl.paginators import CoursePaginator
from app_users.permissions import IsModerator, IsOwner
from app_pwl.serializers.course import CourseSerializer, CourseListSerializer, CourseRetrieveSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()

    default_serializer = CourseSerializer
    serializers = {
        "list": CourseListSerializer,
        "retrieve": CourseRetrieveSerializer,
    }
    pagination_class = CoursePaginator

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def perform_create(self, serializer):
        self.check_permissions(self.request)  # до создания объекта вызываем проверку на права доступа
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

    def create(self, request, *args, **kwargs):
        # Можно создавать только авторизованным пользователям не являющимся модераторами
        self.permission_classes = [~IsModerator]
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # При запросе списка курсов
        # в queryset добавляем поле lesson_count
        # путем подсчета объектов привязанных по ForeignKey
        # по related_name поля course модели Lesson
        self.queryset = self.queryset.annotate(lesson_count=Count('lessons'))
        return super().list(request, *args, **kwargs)

        # Просматривать список может любой авторизованный пользователь (заданно в settings)

    def retrieve(self, request, *args, **kwargs):
        # Можно просматривать только создателю или модератору
        self.permission_classes = [IsOwner | IsModerator]
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Можно изменять только создателю или модератору
        self.permission_classes = [IsOwner | IsModerator]
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Можно удалять только создателю
        self.permission_classes = [IsOwner]
        return super().destroy(request, *args, **kwargs)
