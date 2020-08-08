import uuid
from accounts.models import CustomUser
from django.db import models
import markdown

class Article(models.Model):
    class Meta:
        db_table = 'article'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='記事タイトル', max_length=40)
    content = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_ad = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title

    def markdown_to_html(self):
        md = markdown.Markdown(
            extensions = ['extra', 'admonition', 'sane_lists', 'toc']
        )
        html = md.convert(self.content)
        return html
