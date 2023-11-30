from django.db import models


class Article(models.Model):
    """Model definition for Article"""

    title = models.CharField(
        verbose_name="제목",
        max_length=200
    )
    content = models.TextField(
        verbose_name="본문",
        null=True,
        blank=True,
    )
    created_at = models.DateField(
        verbose_name="생성 날짜",
        auto_now_add=True
    )
    related_posts = models.ManyToManyField(
        'self',
        blank=True
    )
    word_frequencies = models.JSONField(
        default=dict
    )

    class Meta:
        db_table = "article"
        verbose_name = "Article"
        verbose_name_plural = "Articles"
