from django.contrib import admin
from .models import Article
from .models import Tag
from markdownx.admin import MarkdownxModelAdmin

class AirticleAdmin(MarkdownxModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Article, AirticleAdmin)
admin.site.register(Tag)