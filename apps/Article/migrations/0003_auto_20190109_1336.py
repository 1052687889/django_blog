# Generated by Django 2.1.4 on 2019-01-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_auto_20190109_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default=0, verbose_name='博客内容'),
        ),
    ]