from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework import renderers
from snippets.views import api_root, SnippetViewSet, UserViewSet, TaskViewSet, RegisterViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .routers import CustomRouter

router = DefaultRouter()
router.register(r'register', views.RegisterViewSet, basename='register')
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]