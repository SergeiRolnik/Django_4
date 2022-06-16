from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, ArticleScope

class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0  # счетчик того, сколько раз встречается is_main == True
        for form in self.forms:
            count += int(form.cleaned_data.get('is_main', 0))
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        elif count == 2:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]