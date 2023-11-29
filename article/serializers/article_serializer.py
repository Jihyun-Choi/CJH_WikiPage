from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer definition for Article Model."""
    related_posts = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Article.objects.all(),  # TODO
        required=False,  # 필드를 선택적으로 만듭니다.
    )

    class Meta:
        """Meta definition for ArticleSerializer."""

        model = Article

        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "related_posts",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "related_posts",
        ]
