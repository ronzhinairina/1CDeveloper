from django.contrib import admin
from .models import *


class ContentAdminInline(admin.StackedInline):
    model = Content
    extra = 1


class BlockAdmin(admin.ModelAdmin):
    inlines = (ContentAdminInline, )


admin.site.register(Content)
admin.site.register(Block, BlockAdmin)
