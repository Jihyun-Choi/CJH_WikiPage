from django.db import models


class ArticleWord(models.Model):
    """
    - is_common : 전체 게시글 중에 60% 이상 발견되는 단어임을 나타내는 값
        True - 60% 이상 발견되는 단어, 연관게시글 기준에 사용되지 않는 단어.
        False - 60% 이상 발견되지 않는 단어, 연관게시글 기준에 사용되는 단어.
    """
    word = models.CharField(
        max_length=100
    )
    frequency = models.IntegerField(
    )
    is_common = models.BooleanField(
        default=False
    )
