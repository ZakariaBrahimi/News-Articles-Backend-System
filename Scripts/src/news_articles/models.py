from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class NewsArticle(models.Model):
    published_status_options = (
        ('draft' , 'Draft'),
        ('published', 'Published')
    )
    summary          = models.TextField()
    content          = models.TextField()
    title            = models.CharField(max_length=300)
    published_date   = models.DateTimeField(auto_now_add=True)
    category         = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE)
    author           = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    published_status = models.CharField(max_length=15, choices=published_status_options, default='draft')
    bookmark         = models.ManyToManyField(to=User, default=None, blank=True, related_name='bookmark')

    def __str__(self):
        return self.title

class ArticleCategory(models.Model):
    category_name = models.CharField(max_length=50)