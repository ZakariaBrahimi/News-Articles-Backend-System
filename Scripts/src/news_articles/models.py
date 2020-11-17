from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class NewsArticle(models.Model):
    published_status_options = (
        ('draft' , 'Draft'),
        ('published', 'Published')
    )
    cayegory_options = (
        ('politics', 'Politics'),
        ('health', 'Health'),
        ('education', 'Education'),
    )
    title            = models.CharField(max_length=300)
    summary          = models.TextField()
    content          = models.TextField()
    published_status = models.CharField(max_length=15, choices=published_status_options, default='draft')
    published_date   = models.DateTimeField(auto_now_add=True)
    author           = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    category           = models.CharField(max_length=15, choices=cayegory_options,)
    bookmark         = models.ManyToManyField(to=User, default=None, blank=True, related_name='bookmark')

    def __str__(self):
        return self.title