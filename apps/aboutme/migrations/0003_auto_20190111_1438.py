# Generated by Django 2.1.4 on 2019-01-11 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0002_zan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zan',
            old_name='zan_num',
            new_name='num',
        ),
    ]
