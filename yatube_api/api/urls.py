from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

routerv1 = routers.DefaultRouter()
routerv1.register('posts', PostViewSet, basename='posts')
routerv1.register('groups', GroupViewSet, basename='groups')
routerv1.register(r'posts/(?P<post_id>\d+)/comments',
                  CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(routerv1.urls)),
]
