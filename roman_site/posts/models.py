from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


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
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    ) 
