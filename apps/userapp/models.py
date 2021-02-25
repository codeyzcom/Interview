from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    first_name = models.CharField(
        max_length=240,
        verbose_name='Имя'
    )
    middle_name = models.CharField(
        max_length=240,
        verbose_name='Отчество',
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=240,
        verbose_name='Фамилия',
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Возраст'
    )
    position = models.ForeignKey(
        'dictionary.Position',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Должность'
    )
    level = models.ForeignKey(
        'dictionary.Level',
        on_delete=models.PROTECT,
        verbose_name='Уровень'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
