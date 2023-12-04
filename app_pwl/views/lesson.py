from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app_pwl.models import Lesson
from app_pwl.paginators import LessonPaginator
from app_users.permissions import IsModerator, IsOwner
from app_pwl.serializers.lesson import LessonSerializer, LessonListSerializer, LessonCreateSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """ Create a new lesson """

    serializer_class = LessonCreateSerializer

    # Можно создавать только авторизованным пользователям не являющимся модераторами
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """ Get lesson list """

    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator

    # Просматривать список может любой авторизованный пользователь (заданно в settings)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """ Get lesson """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # Можно просматривать только создателю или модератору
    permission_classes = [IsOwner | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """ Update lesson """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # Можно изменять только создателю или модератору
    permission_classes = [IsOwner | IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Delete lesson """

    queryset = Lesson.objects.all()

    # Можно удалять только создателю
    permission_classes = [IsOwner]
