from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, CommentViewSet, ProfileViewSet, ImageCaptionView, PostListCreateView

router = DefaultRouter()
#router.register(r'messages', MessageViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'profiles', ProfileViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('captions/', ImageCaptionView.as_view()),
    path('posts/', PostListCreateView.as_view(), name="post-list"),

]
