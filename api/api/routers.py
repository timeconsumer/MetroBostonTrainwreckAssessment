from rest_framework import routers
from article.viewsets import ArticleViewSet
from trains.viewsets import TrainViewSet

router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)
router.register(r'trains', TrainViewSet)
