from django.db import models

from app_users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Превью", **NULLABLE)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['name', 'description', 'image', ]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", related_name="lessons")
    image = models.ImageField(verbose_name="Превью", **NULLABLE)
    video = models.CharField(max_length=150, verbose_name="Ссылка на видео", **NULLABLE)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['name', 'description', 'course', 'image', 'video', ]

    def __str__(self):
        return self.name
