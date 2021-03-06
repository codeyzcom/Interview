# Generated by Django 3.1.7 on 2021-02-25 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_position'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kernel', '0002_interviewquestion_framework'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalInterviewTask',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Наименование')),
                ('score', models.IntegerField(verbose_name='Балл')),
                ('task', models.TextField(verbose_name='Задача')),
                ('answer', models.TextField(verbose_name='Верный ответ')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dictionary.language', verbose_name='Язык программирования')),
                ('level', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dictionary.level', verbose_name='Уровень')),
            ],
            options={
                'verbose_name': 'historical Задача собеседования',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalInterviewQuestion',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Наименование')),
                ('score', models.IntegerField(verbose_name='Балл')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Верный ответ')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('framework', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dictionary.framework', verbose_name='Фреймворк')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dictionary.language', verbose_name='Язык программирования')),
                ('level', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dictionary.level', verbose_name='Уровень')),
            ],
            options={
                'verbose_name': 'historical Вопрос собеседования',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
