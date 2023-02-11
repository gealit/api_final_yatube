from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet, 'posts')
router.register(r'groups', GroupViewSet, 'groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, 'comments')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/jwt/create/', TokenObtainPairView.as_view()),
    path('v1/jwt/refresh/', TokenRefreshView.as_view()),
    path('v1/jwt/verify/', TokenVerifyView.as_view()),
]
