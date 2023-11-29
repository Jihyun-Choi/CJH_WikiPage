from rest_framework.viewsets import ModelViewSet

from article.models import Article
from article.serializers import ArticleListSerializer, ArticleSerializer
from django.db import transaction
from rest_framework.response import Response

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet


class ArticleViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                     DestroyModelMixin, GenericViewSet):

    def get_queryset(self):
        return Article.objects.all()

    def get_serializer_class(self):
        if self.action == "create" or self.action == "retrieve":
            return ArticleSerializer
        return ArticleListSerializer

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        context = {"request": self.request, "format": self.format_kwarg, "view": self}

        return context

    @transaction.atomic
    def perform_create(self, serializer):
        article = serializer.save()

        # TODO: 연관게시글 저장

        return article

    def create(self, request, *args, **kwargs):
        """
        글을 게시합니다.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        글의 상세 내용을 반환합니다.
        """

        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        글을 삭제합니다.
        """
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        글의 목록을 반환합니다.
        """
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
