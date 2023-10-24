import random
import re
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils.text import slugify
from django.db.models import Sum

def validate_image_extension(value):
    allowed_extensions = ['jpg', 'jpeg', 'png']
    extension = value.name.split('.')[-1].lower()
    if extension not in allowed_extensions:
        raise models.ValidationError("Only JPEG, JPG, and PNG images are allowed.")


def blog_docs_directory(instance, filename):
    return "/".join(["documents", str(instance.author.first_name), "image", filename])


class SubjectCategory(models.Model):
    subject_category_choices = (
        ('unknown', 'UNKNOWN'),
        # ('verve', 'VERVE'),
        # ('mastercard', 'MASTERCARD')
    )

    DEFAULT_CATEGORY_CHOICE = 'unknown'

    subject_category  = models.CharField(
        max_length=16,
        default=DEFAULT_CATEGORY_CHOICE,
        choices=subject_category_choices
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject_category


class Subject(models.Model):
    subject = models.CharField(max_length=200)
    subject_category  = models.ForeignKey(SubjectCategory, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject

class Platform(models.Model):

    platform_choices = (
        ('others', 'OTHERS'),
        ('blog', 'BLOG'),
        ('technical blog', 'TECHNICAL BLOG'),
        ('comment on course pages', 'COMMENT ON COURSE PAGES')
    )

    DEFAULT_PLATFORM_CHOICE = 'others'

    platform = models.CharField(
        max_length=50,
        choices=platform_choices,
        default=DEFAULT_PLATFORM_CHOICE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.platform


class Tag(models.Model):

    tag = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.tag

    def save(self, *args, **kwargs):
        self.tag = self.tag.lower()
        if not self.slug:
            # Generate a unique slug from the title
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):

        # Generate a unique slug based on the title
        base_slug = slugify(self.tag)
        slug = base_slug
        # Generate a random integer between 1000000 and 1000000000000
        counter = 1 #random.randint(1000000, 1000000000000000)

        while Blog.objects.filter(slug=slug).exists():
            # If a blog with the same slug already exists, append a counter to make it unique
            counter += 1 #random.randint(1000000, 1000000000000000)
            slug = f"{base_slug}-{counter}"

        return slug.lower()


class Blog(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)
    content = RichTextField()
    content_url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)
    image = models.ImageField(upload_to=blog_docs_directory, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    created_at = models.DateTimeField(auto_now_add=True)

    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING, related_name="blog_platform")
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, related_name="blog_tag")
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name="blog_subject")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.capitalize()
        # Check if the author is not already set (i.e., it's a new blog)
        if not self.author_id:
            # Set the author to the admin user (assuming admin user is the first user in the User table)
            admin_user = get_user_model().objects.first()
            self.author = admin_user
        if not self.slug:
            # Generate a unique slug from the title
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        # Remove non-letter characters from the title
        re.sub(r'[^a-zA-Z]+', '', self.title)
        # Generate a unique slug based on the title
        temp = f"{self.tag.slug}-{self.title.lower()}"
        base_slug = slugify(temp)
        slug = base_slug
        # Generate a random integer between 1000000 and 1000000000000
        counter = random.randint(1000000, 1000000000000000)

        while Blog.objects.filter(slug=slug).exists():
            # If a blog with the same slug already exists, append a counter to make it unique
            counter = random.randint(1000000, 1000000000000000)
            slug = f"{base_slug}-{counter}"

        return slug.lower()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    #Commentator user
    commentator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', blank=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commentator.first_name} on {self.blog.title}"

class ReplyComment(models.Model):
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"Reply to Comment #{self.comment.id} - Reply #{self.id}"
