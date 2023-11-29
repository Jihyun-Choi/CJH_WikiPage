from article.views import ArticleViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "article"

router = DefaultRouter()
router.register("", ArticleViewSet, basename="Article")

urlpatterns = [
]

urlpatterns += router.urls
