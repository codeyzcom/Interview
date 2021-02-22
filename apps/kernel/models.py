from django.db import models


class InterviewTask(models.Model):
    class Meta:
        verbose_name = 'Задача собеседования'
        verbose_name_plural = 'Задачи собеседования'

    name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name='Наименование'
    )
    score = models.IntegerField(
        verbose_name='Балл'
    )
    language = models.ForeignKey(
        'dictionary.Language',
        on_delete=models.PROTECT,
        verbose_name='Язык программирования'
    )
    level = models.ForeignKey(
        'dictionary.Level',
        on_delete=models.PROTECT,
        verbose_name='Уровень'
    )
    task = models.TextField(
        verbose_name='Задача'
    )
    answer = models.TextField(
        verbose_name='Верный ответ'
    )

    def __str__(self):
        return self.name


class InterviewQuestion(models.Model):
    class Meta:
        verbose_name = 'Вопрос собеседования'
        verbose_name_plural = 'Вопросы собеседования'

    name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name='Наименование'
    )
    score = models.IntegerField(
        verbose_name='Балл'
    )
    language = models.ForeignKey(
        'dictionary.Language',
        on_delete=models.PROTECT,
        verbose_name='Язык программирования'
    )
    level = models.ForeignKey(
        'dictionary.Level',
        on_delete=models.PROTECT,
        verbose_name='Уровень'
    )
    framework = models.ForeignKey(
        'dictionary.Framework',
        on_delete=models.PROTECT,
        verbose_name='Фреймворк',
        null=True,
        blank=True,
    )
    question = models.TextField(
        verbose_name='Вопрос'
    )
    answer = models.TextField(
        verbose_name='Верный ответ'
    )

    def __str__(self):
        return self.name


class Interview(models.Model):
    class Meta:
        verbose_name = 'Собеседование'
        verbose_name_plural = 'Собеседования'

    date = models.DateTimeField(
        verbose_name='Дата проведения собеседования'
    )
    user = models.ForeignKey(
        'userapp.Profile',
        on_delete=models.PROTECT,
        verbose_name='Сотрудник'
    )
    question = models.ManyToManyField(
        'InterviewQuestion',
        through='InterviewQuestionToInterview',
        verbose_name='Вопросы'
    )
    task = models.ManyToManyField(
        'InterviewTask',
        through='InterviewTaskToInterview',
        verbose_name='Задачи'
    )
    result_level = models.ForeignKey(
        'dictionary.Level',
        related_name='result_level',
        on_delete=models.DO_NOTHING,
        verbose_name='Уровень по результату',
        help_text='Уровень присвоенный по результату собеседования',
        null=True,
        blank=True
    )
    target_level = models.ForeignKey(
        'dictionary.Level',
        related_name='target_level',
        on_delete=models.DO_NOTHING,
        verbose_name='Заявленный уровень',
        null=True,
        blank=True
    )
    total_score = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Суммарный балл'
    )
    note = models.TextField(
        null=True,
        blank=True,
        verbose_name='Заключение'
    )


class InterviewQuestionToInterview(models.Model):
    class Meta:
        verbose_name = 'Пул вопросов'
        verbose_name_plural = 'Пул вопросов'

    interview = models.ForeignKey(
        'Interview',
        on_delete=models.DO_NOTHING,
        verbose_name='Собеседование'
    )
    question = models.ForeignKey(
        'InterviewQuestion',
        on_delete=models.DO_NOTHING,
        verbose_name='Вопрос'
    )
    answer_accepted = models.BooleanField(
        default=False,
        verbose_name='Ответ засчитан'
    )
    note = models.TextField(
        null=True,
        blank=True,
        verbose_name='Примечание'
    )


class InterviewTaskToInterview(models.Model):
    class Meta:
        verbose_name = 'Пул задач'
        verbose_name_plural = 'Пул задач'

    interview = models.ForeignKey(
        'Interview',
        on_delete=models.DO_NOTHING,
        verbose_name='Собеседование'
    )
    task = models.ForeignKey(
        'InterviewTask',
        on_delete=models.DO_NOTHING,
        verbose_name='Задача'
    )
    answer_accepted = models.BooleanField(
        default=False,
        verbose_name='Задача решена'
    )
    note = models.TextField(
        null=True,
        blank=True,
        verbose_name='Примечание'
    )
