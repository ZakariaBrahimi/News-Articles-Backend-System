# Generated by Django 3.1.3 on 2020-11-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0004_auto_20201115_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='author',
            field=models.CharField(default=55555, max_length=30),
            preserve_default=False,
        ),
    ]
