from django.db import models

from django.db import models
from django.utils import timezone  # pentru dateTime

class Article(models.Model):
    name = models.CharField('denumire',max_length=100)
    description = models.TextField('text_articol')
    date = models.DateTimeField('data_pub')

    def __str__ (self):
        return self.name

    def recent_pub(self):
        return self.date >=(timezone.now())


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('autor',max_length=50)
    commentary = models.CharField('text_commentariu',max_length=150)

    def __str__ (self):
        return self.author