# Generated by Django 4.1.4 on 2022-12-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(default='', max_length=100)),
                ('auteur', models.CharField(default='', max_length=150)),
                ('description', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
