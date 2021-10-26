from django.contrib import admin

from posts.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


class BlogAdminInLine(admin.StackedInline):
    model = Blog
    extra = 0
    classes = ['collapse']
