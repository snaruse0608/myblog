from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name='記事タイトル', max_length=40)
    content = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_ad = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    
    def __str__(self):
        return self.title
