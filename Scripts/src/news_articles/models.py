from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class NewsArticle(models.Model):
    options = (
        ('draft' , 'Draft'),
        ('published', 'Published')
    )
    title            = models.CharField(max_length=300)
    summary          = models.TextField()
    content          = models.TextField()

    published_status = models.CharField(max_length=15, choices=options, defaulf='draft')
    published_date   = models.DateTimeField(auto_now_add=True)
    author           = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    category         = models.CharField(max_length=20)
    bookmark         = models.ManyToManyField(to=NewsArticle, related_name='bookmark')

    def __str__(self):
        return self.title

# class Bookmark(models.Model):
#     articles = models.ManyToManyField(to=NewsArticle)

    # def __str__(self):
    #     return 'articles_title'

# class Category(models.Model):
#     article = models.OneToOneField(on_delete=)

# class Author(models.Model):
#     name = models.CharField()
