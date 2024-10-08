# Generated by Django 4.2.15 on 2024-08-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('number', models.AutoField(db_column='Number', primary_key=True, serialize=False)),
                ('артикул', models.TextField(blank=True, db_column='Артикул', null=True)),
                ('наименование_ru', models.TextField(blank=True, db_column='Наименование RU', null=True)),
                ('наименование_en', models.TextField(blank=True, db_column='Наименование EN', null=True)),
                ('наименование_de', models.TextField(blank=True, db_column='Наименование DE', null=True)),
                ('hs', models.TextField(blank=True, db_column='HS', null=True)),
                ('описаине', models.TextField(blank=True, db_column='Описаине', null=True)),
                ('вес_нетто', models.TextField(blank=True, db_column='Вес нетто', null=True)),
                ('unnamed_8', models.TextField(blank=True, db_column='Unnamed: 8', null=True)),
                ('image1', models.TextField(blank=True, null=True)),
                ('image2', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Products',
                'managed': False,
            },
        ),
    ]
