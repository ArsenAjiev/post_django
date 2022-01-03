from django.urls import path, include
from post.views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostViewSet, basename='post'),

app_name = 'post'

urlpatterns = [

    path('', include(router.urls)),
]