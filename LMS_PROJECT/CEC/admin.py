from django.contrib import admin
from CEC import models

class SubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "subject_category", "created_at")
    list_display_links = list_display = ("id", "subject_category")

admin.site.register(models.SubjectCategory, SubjectCategoryAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "created_at")
    list_display_links = list_display = ("id", "subject")

admin.site.register(models.Subject, SubjectAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "tag", "created_at")
    list_display_links = ("id", "tag")

admin.site.register(models.Tag, TagAdmin)



class PlatformAdmin(admin.ModelAdmin):
    list_display = ("id", "platform", "created_at")
    list_display_links = list_display = ("id", "platform")

admin.site.register(models.Platform, PlatformAdmin)




class BlogAdmin(admin.ModelAdmin):

    list_display = ('id', 'author', 'title', 'created_at')
    list_display_links = ('id', 'author', 'title')


admin.site.register(models.Blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):

    list_display = ('id', 'commentator', 'created_at')
    list_display_links = ('id', 'commentator')


admin.site.register(models.Comment, CommentAdmin)

class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'comment', 'created_at')
    list_display_links = ('id', 'content')

admin.site.register(models.ReplyComment, ReplyCommentAdmin)
