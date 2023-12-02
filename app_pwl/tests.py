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

        # Считаем количество уроков в базе данных
        lesson_count = Lesson.objects.all().count()

        data = {
            "name": "Test Lesson",
            "description": "Description Test Lesson",
            "course": self.course.id,
        }

        response = self.client.post(
            reverse("app_pwl:lesson_create"),
            data=data
        )

        # Проверяем что объект успешно создан
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Проверяем что в базе данных стало на 1 урок больше
        self.assertEquals(
            Lesson.objects.all().count(),
            lesson_count + 1
        )

    def test_lesson_video_link_validation(self):
        """Тестирование валидации при создании урока с допустимой ссылкой"""

        # Принудительно аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

        link_valid = [
            "https://www.youtube.com/watch?v=qweasdzxc",
            "www.youtube.com/watch?v=qweasdzxc",
            "youtube.com/watch?v=qweasdzxc",
            "https://youtu.be/qweasdzxc",
            "youtu.be/mHQXz5FctRg",
        ]

        for link in link_valid:
            response = self.client.post(
                reverse("app_pwl:lesson_create"),
                data={
                    "name": "Test Lesson",
                    "description": "Description Test Lesson",
                    "course": self.course.id,
                    "video": link
                }
            )

            self.assertEquals(
                response.status_code,
                status.HTTP_201_CREATED
            )

    def test_lesson_video_link_validation_error(self):
        """Тестирование валидации при создании урока с недопустимой ссылкой"""

        # Принудительно аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

        link_invalid = [
            "https://dzen.ru/video/watch/qweasdzxc",
            "dzen.ru/video/watch/qweqweqwe",
            "https://vk.com/video-123123123_123123123",
            "vk.com/video-123123123_123123123",
        ]

        for link in link_invalid:
            response = self.client.post(
                reverse("app_pwl:lesson_create"),
                data={
                    "name": "Test Lesson",
                    "description": "Description Test Lesson",
                    "course": self.course.id,
                    "video": link
                }
            )

            self.assertEquals(
                response.status_code,
                status.HTTP_400_BAD_REQUEST
            )

    def test_lesson_materials_validation(self):
        """
        Тестирование валидации при создании тела урока,
        названия и описания с допустимой ссылкой
        """

        # Принудительно аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

        text_valid_list = [
            "Тест https://www.youtube.com/watch?v=qweasdzxc Ok",
            "Проверка www.youtube.com/watch?v=qweasdzxc link",
            "Проверка youtube.com/watch?v=qweasdzxc link",
            "Проверка https://youtu.be/qweasdzxc link",
            "Проверка youtu.be/mHQXz5FctRg link. qwe/qwe",
        ]

        for text in text_valid_list:
            data_list = [
                {
                    "name": text,
                    "description": "Description Test Lesson",
                    "body": "Test text fo test",
                    "course": self.course.id,
                },
                {
                    "name": "Test Lesson",
                    "description": text,
                    "body": "Test text fo test",
                    "course": self.course.id,
                },
                {
                    "name": "Test Lesson",
                    "description": "Description Test Lesson",
                    "body": text,
                    "course": self.course.id,
                },
            ]
            for data in data_list:
                response = self.client.post(
                    reverse("app_pwl:lesson_create"),
                    data=data
                )

                self.assertEquals(
                    response.status_code,
                    status.HTTP_201_CREATED
                )

    def test_lesson_materials_validation_error(self):
        """
        Тестирование валидации при создании тела урока,
        названия и описания с не допустимой ссылкой
        """

        # Принудительно аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

        text_invalid_list = [
            "Text https://dzen.ru/video/watch/qweasdzxc z. q/w",
            "text dzen.ru/video/watch/qweqweqwe ru, qwe? yu/yu",
            "vid https://vk.com/video-123123123_123123123 go,",
            "nm, vk.com/video-123123123_123123123 jkl",
        ]

        for text in text_invalid_list:
            data_list = [
                {
                    "name": text,
                    "description": "Description Test Lesson",
                    "body": "Test text fo test",
                    "course": self.course.id,
                },
                {
                    "name": "Test Lesson",
                    "description": text,
                    "body": "Test text fo test",
                    "course": self.course.id,
                },
                {
                    "name": "Test Lesson",
                    "description": "Description Test Lesson",
                    "body": text,
                    "course": self.course.id,
                },
            ]
            for data in data_list:
                response = self.client.post(
                    reverse("app_pwl:lesson_create"),
                    data=data
                )

                self.assertEquals(
                    response.status_code,
                    status.HTTP_400_BAD_REQUEST
                )
