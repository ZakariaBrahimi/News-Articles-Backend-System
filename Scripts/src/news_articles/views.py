# from django.shortcuts import render
from .models import NewsArticle
from .serializers import NewsArticlesSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArticlesList(APIView):
    """
    List of all articles.
    """
    def get(self, request ):
        articles = NewsArticle.objects.all()
        serializer = NewsArticlesSerializer(articles, many=True)
        return Response(serializer.data)
