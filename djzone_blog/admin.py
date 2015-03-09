from django.contrib import admin
from django import forms

from taggit.forms import TagWidget

import models


class CustomTagWidget(TagWidget):
    def render(self, name, value, attrs=None):
        widget = super(CustomTagWidget, self).render(name, value, attrs)
        return widget


class ContentForm(forms.ModelForm):
    class Meta:
        model = models.Content
        widgets = {
            'tags': CustomTagWidget(attrs={'data-role': 'tagsinput'}),
        }


class ContentAdmin(admin.ModelAdmin):

    form = ContentForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'published_on', 'is_published')
    list_filter = ('tags',)


admin.site.register(models.Post, ContentAdmin)
admin.site.register(models.NewsItem, ContentAdmin)
admin.site.register(models.Project, ContentAdmin)
