from django.contrib import admin

from article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin View for Article"""

    list_display = (
        "title",
        "content",
        "created_at",
        "display_related_posts",  # 연관된 게시글의 id 리스트
    )

    def display_related_posts(self, obj):
        related_post_ids = [str(related_post.id) for related_post in obj.related_posts.all()]
        return ", ".join(related_post_ids)
    display_related_posts.short_description = "Related Post IDs"
