from django.db import models

from app_users.models import NULLABLE, User
from config import settings
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(verbose_name=_("image"), **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Owner"), **NULLABLE)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['name', 'description', 'image', ]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", related_name="lessons")
    body = models.TextField(verbose_name=_("Lesson Materials"), **NULLABLE)
    image = models.ImageField(verbose_name=_("image"), **NULLABLE)
    video = models.CharField(max_length=150, verbose_name=_("Link to video"), **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Owner"), **NULLABLE)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['name', 'description', 'course', 'image', 'video', ]

    def __str__(self):
        return self.name
