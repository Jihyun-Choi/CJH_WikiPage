# Generated by Django 4.0.6 on 2023-11-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('content', models.TextField(blank=True, null=True, verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('related_posts', models.ManyToManyField(blank=True, to='article.article')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'db_table': 'article',
            },
        ),
    ]
