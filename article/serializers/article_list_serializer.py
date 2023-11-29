from rest_framework import serializers

from article.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    """Serializer definition for Article Model."""

    class Meta:
        """Meta definition for ArticleListSerializer."""

        model = Article

        fields = [
            "id",
            "title",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "title",
            "created_at",
        ]
