import re
from collections import Counter


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
