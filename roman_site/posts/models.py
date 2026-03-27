from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    tag = models.CharField('Тег', max_length=20)
    
    def __str__(self):
        return self.tag


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
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте Ctrl для выбора нескольких вариантов'
    ) 


class Comment(models.Model):
    text = models.TextField('Текст')
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
