from django.db import models


class Level(models.Model):
    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    name = models.CharField(
        max_length=64,
        verbose_name='Наименование'
    )

    def __str__(self):
        return self.name


class Language(models.Model):
    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    name = models.CharField(
        max_length=64,
        verbose_name='Наименование'
    )

    def __str__(self):
        return self.name


class Framework(models.Model):
    class Meta:
        verbose_name = 'Фреймворк'
        verbose_name_plural = 'Фреймворки и библиотеки'

    name = models.CharField(
        max_length=128,
        verbose_name='Наименование'
    )
    language = models.ForeignKey(
        'Language',
        on_delete=models.PROTECT,
        verbose_name='Язык программирования'
    )

    def __str__(self):
        return f'{self.language}: {self.name}'
