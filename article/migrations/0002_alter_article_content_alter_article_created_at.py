# Generated by Django 4.0.6 on 2023-11-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='본문'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='생성 날짜'),
        ),
    ]
