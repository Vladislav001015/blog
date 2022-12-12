from django.urls import path, include
from applications.post.views import PostAPIView, CategoryAPIView, CommentAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('category', CategoryAPIView)
router.register('comment', CommentAPIView)
router.register('', PostAPIView)


urlpatterns = [
    # path('', PostAPIView.as_view({'get': 'list', 'post': 'create'}))
    # path('', include(router.urls))
]

urlpatterns += router.urls