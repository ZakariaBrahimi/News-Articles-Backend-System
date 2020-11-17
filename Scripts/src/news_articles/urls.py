from django.urls import path
from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticlesList
app_name = 'news_articles'


urlpatterns = [
    url('articles/', ArticlesList.as_view()),
]