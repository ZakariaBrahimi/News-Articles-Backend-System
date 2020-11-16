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
    # published_status = models.BooleanField(default= False)
    published_status = models.CharField(max_length=15, choices=options, default='draft')
    published_date   = models.DateTimeField(auto_now_add=True)
    author           = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    category         = models.CharField(max_length=20)
    bookmark         = models.ManyToManyField(to=User, default=None, blank=True)

    def __str__(self):
        return self.title


# class Category(models.Model):
#     article = models.OneToOneField(on_delete=)