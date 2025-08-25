from django.contrib import admin
from .models import Article, Memo

# Register your models here.
# @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_short','created_at')

    def content_short(self, article):
        return article.content[:10]
    content_short.short_description = '간략한 내용'

admin.site.register(Article, ArticleAdmin)


@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_important', 'created_at']
    list_filter = ['is_important', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_important']  # 목록에서 바로 수정 가능!