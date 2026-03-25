from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Post(models.Model):
    title = models.CharField('title', max_length=50)
    desc = models.TextField('text', max_length=100)
    year = models.IntegerField(
        'year',
        validators=[
            MaxValueValidator(1453), 
            MinValueValidator(-756)
        ],
    )
    pub_date = models.DateTimeField(
        'pub date',
        auto_now_add=True
    )
