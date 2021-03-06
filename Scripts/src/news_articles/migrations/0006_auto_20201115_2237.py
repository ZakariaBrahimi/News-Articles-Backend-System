# Generated by Django 3.1.3 on 2020-11-15 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_articles', '0005_newsarticle_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='bookmark',
            field=models.ManyToManyField(related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
