# Generated by Django 4.1.1 on 2022-09-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='название')),
                ('rate', models.FloatField(verbose_name='курс к рублю')),
            ],
            options={
                'verbose_name': 'валюта',
                'verbose_name_plural': 'валюты',
            },
        ),
    ]
