 
from django.contrib import admin
from django.urls import path,include
from .views import ArticleList, ArticleDetails ,ArticleViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewsets, basename='articles')


urlpatterns = [
    path('articles', ArticleList.as_view()),
    path('api',include(router.urls)),
   # path('articles/<int:pk>', ArticleDetails.as_view() ),

   # path('articles/<int:pk>', article_detail),


]
