# Generated by Django 2.1.4 on 2019-01-09 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name='阅读数'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Article.Category', verbose_name='分类'),
        ),
    ]
