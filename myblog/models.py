import uuid
from accounts.models import CustomUser
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Tag(models.Model):
    class Meta:
        db_table = 'tag'

    name = models.CharField(verbose_name='タグ名', max_length=255)

    def __str__(self):
        return self.name

class Article(models.Model):
    class Meta:
        db_table = 'article'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='記事タイトル', max_length=40)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.PROTECT)
    content = MarkdownxField('本文', help_text='マークダウン形式で記述してください')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_ad = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    
    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.content)
