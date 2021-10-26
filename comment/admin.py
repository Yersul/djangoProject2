from django.contrib import admin
# Register your models here.
from mptt.admin import MPTTModelAdmin
from .models import Comment

# class CommentAdminInLine(admin.StackedInline):
#     model = Comment
#     extra = 0
#     classes = ['collapse']
#
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     inlines = [
#         CommentAdminInLine,
#     ]

admin.site.register(Comment)


# Register your models here.
