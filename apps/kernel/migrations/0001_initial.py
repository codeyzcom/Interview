# Generated by Django 3.1.7 on 2021-02-22 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionary', '0001_initial'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата проведения собеседования')),
                ('total_score', models.FloatField(blank=True, null=True, verbose_name='Суммарный балл')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заключение')),
            ],
            options={
                'verbose_name': 'Собеседование',
                'verbose_name_plural': 'Собеседования',
            },
        ),
        migrations.CreateModel(
            name='InterviewQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Наименование')),
                ('score', models.IntegerField(verbose_name='Балл')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Верный ответ')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dictionary.language', verbose_name='Язык программирования')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dictionary.level', verbose_name='Уровень')),
            ],
            options={
                'verbose_name': 'Вопрос собеседования',
                'verbose_name_plural': 'Вопросы собеседования',
            },
        ),
        migrations.CreateModel(
            name='InterviewTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Наименование')),
                ('score', models.IntegerField(verbose_name='Балл')),
                ('task', models.TextField(verbose_name='Задача')),
                ('answer', models.TextField(verbose_name='Верный ответ')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dictionary.language', verbose_name='Язык программирования')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dictionary.level', verbose_name='Уровень')),
            ],
            options={
                'verbose_name': 'Задача собеседования',
                'verbose_name_plural': 'Задачи собеседования',
            },
        ),
        migrations.CreateModel(
            name='InterviewTaskToInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_accepted', models.BooleanField(default=False, verbose_name='Задача решена')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Примечание')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kernel.interview', verbose_name='Собеседование')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kernel.interviewtask', verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'Пул задач',
                'verbose_name_plural': 'Пул задач',
            },
        ),
        migrations.CreateModel(
            name='InterviewQuestionToInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_accepted', models.BooleanField(default=False, verbose_name='Ответ засчитан')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Примечание')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kernel.interview', verbose_name='Собеседование')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kernel.interviewquestion', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Пул вопросов',
                'verbose_name_plural': 'Пул вопросов',
            },
        ),
        migrations.AddField(
            model_name='interview',
            name='question',
            field=models.ManyToManyField(through='kernel.InterviewQuestionToInterview', to='kernel.InterviewQuestion', verbose_name='Вопросы'),
        ),
        migrations.AddField(
            model_name='interview',
            name='result_level',
            field=models.ForeignKey(blank=True, help_text='Уровень присвоенный по результату собеседования', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='result_level', to='dictionary.level', verbose_name='Уровень по результату'),
        ),
        migrations.AddField(
            model_name='interview',
            name='target_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='target_level', to='dictionary.level', verbose_name='Заявленный уровень'),
        ),
        migrations.AddField(
            model_name='interview',
            name='task',
            field=models.ManyToManyField(through='kernel.InterviewTaskToInterview', to='kernel.InterviewTask', verbose_name='Задачи'),
        ),
        migrations.AddField(
            model_name='interview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='userapp.profile', verbose_name='Сотрудник'),
        ),
    ]
