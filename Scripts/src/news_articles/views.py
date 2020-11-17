# from django.shortcuts import render
from .models import NewsArticle
from .serializers import NewsArticlesSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class ArticlesList(APIView):
    """
    List of all articles.
    """
    def get(self, request):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
            print(Token.objects.get_or_create(user=user))
        articles = NewsArticle.objects.all()
        serializer = NewsArticlesSerializer(articles, many=True)
        return Response(serializer.data)
