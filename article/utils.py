import re
from collections import Counter
from article.models.article_word import ArticleWord


def calculate_word_frequencies(content):
    """
    - 게시글의 내용을 단어와 단어의 빈도수를 딕셔너리로 저장하여 반환하는 함수.
    - 게시글의 내용을 모두 소문자로 변환하고, 특수문자를 제거하는 전처리 과정을 진행.
    - 공백을 기준으로 단어를 분리 후 Counter()를 이용하여 딕셔너리 형태로 저장.
    """
    content = content.lower()
    content = re.sub(r'[^a-z0-9\s]', '', content)
    word_counts = Counter(content.split())
    return dict(word_counts)


def update_word_common_status():
    """
    - ArticleWord의 is_common 값을 update 하는 함수.
    - ArticleWord에 저장된 전체 단어의 빈도의 합을 계산하여 threshold 저장.
    - threshold 값을 기반으로 is_common값을 update함.
    - 게시글이 매우 많아질 경우 성능에 문제가 생길 위험이 있음.
    - 추후 함수를 주기적으로 실행하는 배치 작업으로 구성하거나, 비동기적으로 실행하여 성능을 개선.
    """
    total_frequency = sum(word_entry.frequency for word_entry in ArticleWord.objects.all())
    threshold = total_frequency * 0.6  # 전체 단어 빈도의 60%를 계산

    for word_entry in ArticleWord.objects.all():
        # 각 단어의 빈도가 전체 단어 빈도의 60% 이상인지 확인
        word_entry.is_common = word_entry.frequency >= threshold
        word_entry.save()

    # TODO: ArticleWord의 is_common 수정 시 전체 게시글의 연관게시글 변경
