# Generated by Django 3.1.7 on 2021-02-22 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=240, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=240, null=True, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=240, verbose_name='Фамилия')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('position', models.CharField(blank=True, max_length=128, null=True, verbose_name='Должность')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dictionary.level', verbose_name='Уровень')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]