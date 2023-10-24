from rest_framework import serializers
from .models import Blog, Comment, ReplyComment

class ReplyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    commentator_name = serializers.SerializerMethodField()
    blog_title = serializers.SerializerMethodField()
    content = serializers.CharField()
    replies = ReplyCommentSerializer(many=True, read_only=True)

    def get_blog_title(self, obj):
        return obj.blog.title

    def get_commentator_name(self, obj):
        return obj.commentator.first_name + " " + obj.commentator.last_name

    class Meta:
        model = Comment
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    author_name = serializers.SerializerMethodField()
    slug = serializers.CharField()
    image = serializers.ImageField()
    content = serializers.CharField()
    platform = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    def get_author_name(self, obj):
        return obj.author.first_name if obj.author.first_name != "" else "Administrator"

    def get_platform(self, obj):
        return obj.platform.platform

    def get_tag(self, obj):
        return obj.tag.tag

    def get_subject(self, obj):
        return obj.subject.subject

    class Meta:
        model = Blog
        fields = "__all__"
