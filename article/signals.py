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


def update_related_articles(instance):
    """
    - 연관게시글을 찾아내는 함수
    - is_common이 False인 단어들과 생성된 게시글의 word_frequencies 단어들의 공통된 단어들을 추출
    - 다른 모든 Article 객체를 순회하며 연관 게시글 탐색
    - 공통 단어별 빈도의 합산을 기준으로 연관순위 정렬
    - 연관 게시글을 related_posts 필드에 저장
    """
    low_freq_words = set(ArticleWord.objects.filter(is_common=False).values_list('word', flat=True))
    common_words = set(instance.word_frequencies.keys()).intersection(low_freq_words)

    related_articles = []
    for article in Article.objects.exclude(id=instance.id):
        article_common_words = set(article.word_frequencies.keys()).intersection(common_words)
        if len(article_common_words) >= 2:
            related_articles.append(article)
    instance.related_posts.set(related_articles)  # 연관 게시글을 related_posts 필드에 저장

    related_articles.sort(key=lambda x: x[1], reverse=True)

    for related_article in related_articles:  # 각 연관 게시글의 related_posts 필드에도 새 게시글을 추가
        related_article.related_posts.add(instance)
        related_article.save()
        # TODO: 연관 게시글이 추가된 게시글들의 연관 순위 재정렬


@receiver(post_save, sender=Article)
def article_post_save_handler(sender, instance, created, **kwargs):
    """
    - Article 객체가 생성될 때 호출되는 함수
    """
    if created:
        update_article_word(instance)
        update_word_common_status()
        update_related_articles(instance)
