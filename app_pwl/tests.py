from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_pwl.models import Lesson, Course
from app_users.models import User


class CourseTest(APITestCase):
    pass


class LessonTest(APITestCase):
    def setUp(self):
        # User
        self.user = User.objects.create(
            email="test@test.com",
            is_staff=False,
            is_active=True,
        )
        self.user.set_password('test')
        self.user.save()

        # Course
        self.course = Course.objects.create(
            name="Test Course",
            description="Description Test Course"
        )

        # Lessons
        self.lesson1 = Lesson.objects.create(
            name="Test Lesson 1",
            description="Description Test Lesson 1",
            course=self.course,
        )
        self.lesson2 = Lesson.objects.create(
            name="Test Lesson 2",
            description="Description Test Lesson 2",
            course=self.course,
        )

    def test_lesson_create(self):
        """Тестирование создания урока"""

        # Принудительно аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

        data = {
            "name": "Test Lesson",
            "description": "Description Test Lesson",
            "course": "1",
        }

        response = self.client.post(
            reverse("app_pwl:lesson_create"),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            Lesson.objects.all().count(),
            3
        )

    def test_lesson_creat_validation_error(self):
        """Тестирование валидации при создании урока"""

        # Принудительно аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

        data_valid = {
            "name": "Test Lesson",
            "description": "Description Test Lesson",
            "course": "1",
            "video": "https://www.youtube.com/watch?v=cfJrtx-k96U&pp=ygUV0YPRgNC-0Log0LfQvdC10YDRidGC"
        }

        data_invalid = {
            "name": "Test Lesson",
            "description": "Description Test Lesson",
            "course": "1",
            "video": "https://dzen.ru/video/watch/6560c727888ea253658647c4"
        }

        # Проверка заведома правильной ссылки
        response = self.client.post(
            reverse("app_pwl:lesson_create"),
            data=data_valid
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Проверка неправильной ссылки
        response = self.client.post(
            reverse("app_pwl:lesson_create"),
            data=data_invalid
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
