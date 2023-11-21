from django.urls import path
from rest_framework import routers

from app_pwl.views.course import *
from app_pwl.views.lesson import *

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view()),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view()),
    path('lesson/create/', LessonCreateAPIView.as_view()),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view()),
    path('lesson/<int:pk>/destroy/', LessonDestroyAPIView.as_view()),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
