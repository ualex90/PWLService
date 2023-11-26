from django.db import models

from app_pwl.models import Course, Lesson
from app_users.models import User, NULLABLE


class Payment(models.Model):

    # Choices для способа оплаты
    TRANSFER = "transfer"
    CASH = "cash"

    PAYMENT_METHOD_CHOICES = [
        (TRANSFER, 'Перевод на счет'),
        (CASH, 'Наличные'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE)
    payment_amount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=8, choices=PAYMENT_METHOD_CHOICES, verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        purpose = f"Курс: {self.course.name}" if self.course else (f"Курс: {self.lesson.course.name}\n"
                                                                   f"Урок: {self.lesson.name}")
        return f'{self.user}\n{self.date}\n{purpose}'
