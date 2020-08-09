import uuid
from accounts.models import CustomUser
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Article(models.Model):
    class Meta:
        db_table = 'article'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='記事タイトル', max_length=40)
    content = MarkdownxField('Content', help_text='To Write with Markdown format')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_ad = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.PROTECT)

    
    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.content)