# Generated by Django 3.2.11 on 2022-01-05 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=64, verbose_name='Регион')),
                ('city', models.CharField(max_length=64, verbose_name='Город')),
                ('street', models.CharField(max_length=64, verbose_name='Улица')),
                ('house', models.CharField(max_length=64, verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Источник',
                'verbose_name_plural': 'Источники',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(blank=True, verbose_name='Год ввода дома в эксплуатацию')),
                ('floors', models.PositiveSmallIntegerField(blank=True, verbose_name='Количество этажей')),
                ('updating', models.DateField(blank=True, verbose_name='Последнее актуализирование информации')),
                ('series', models.CharField(blank=True, max_length=64, verbose_name='Серия, тип постройки здания')),
                ('type_of_building', models.CharField(blank=True, max_length=64, verbose_name='Тип дома')),
                ('emergency', models.CharField(blank=True, max_length=64, verbose_name='Факт признания дома аварийным')),
                ('cadastre', models.CharField(blank=True, max_length=64, verbose_name='Кадастровый номер земельного участка')),
                ('floor', models.CharField(blank=True, max_length=64, verbose_name='Тип перекрытий')),
                ('walls', models.CharField(blank=True, max_length=64, verbose_name='Материал несущих стен')),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_parser.source', verbose_name='Источник')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
    ]