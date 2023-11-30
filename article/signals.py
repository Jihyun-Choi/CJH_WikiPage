from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article, ArticleWord
from .utils import update_word_common_status


def update_article_word(instance):
    """
    - Article 본문 내용에 존재하는 단어와 단어의 빈도수를 저장한 word_frequencies를 기반으로,
        ArticleWord 객체를 생성 및 수정하는 함수
    - ArticleWord에 이미 존재하는 단어라면 frequency 빈도 수를 증가
    - ArticleWord에 존재하지 않는 단어라면, 단어를 생성 후 frequency 빈도 수를 추가
    """
    for word, frequency in instance.word_frequencies.items():
        word_entry, _ = ArticleWord.objects.get_or_create(word=word)
        word_entry.frequency += frequency
        word_entry.save()


@receiver(post_save, sender=Article)
def article_post_save_handler(sender, instance, created, **kwargs):
    """
    - Article 객체가 생성될 때 호출되는 함수
    """
    if created:
        update_article_word(instance)
