from django.db import models
import uuid
from CSRM.models import CSRM_Institution
from CAT.models import CAT_Instructor


class CEC_Course(models.Model):

    level_choices = (
        ('I', 'INTRODUCTORY'),
        ('IN', 'INTERMEDIATE'),
        ('A', 'ADVANCED'),
    )
    pacing_choices = (
        ('I', 'INSTRUCTOR-LED'),
        ('S', 'SELF-PACED'),
    )
    enrollment_choices = (
        ('O', 'OPEN'),
        ('B', 'BY_INVITATION'),
    )
    lang_choices = (
        ('E', 'ENGLISH'),
        ('F', 'FRENCH'),
        ('C', 'CHINESE'),
        ('Y', 'YORUBA'),
        ('H', 'HAUSA'),
        ('I', 'IGBO')
    )
    publication_choices = (
        ('DN', 'DRAFT(NEVER PUBLISHED)'),
        ('P', 'PUBLISHED(NOT YET RELEASED)'),
        ('PL', 'PUBLISHED AND LIVE'),
        ('DU', 'DRAFT(UNPUBLISHED CHANGES)'),
    )
    learning_choices = (
        ('S', 'SELF PACED'),
        ('I', 'INSTRUCTOR LED'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    code = models.CharField(max_length=10, null=False)
    version = models.IntegerField(null=True, blank=True)
    created_by_id = models.ForeignKey(CAT_Instructor, on_delete=models.CASCADE,  null=True)
    institution_id = models.ForeignKey(CSRM_Institution, on_delete=models.CASCADE, null=True)
    semester = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True)
    short_description = models.CharField(max_length=250, null=True, blank=True)
    overview = models.FileField(upload_to=None, blank=True, null=True)
    level = models.CharField(choices=level_choices, max_length=4, default="I",blank=True, null=True)
    course_pacing = models.CharField(choices=pacing_choices, max_length=4, default="I", blank=True, null=True)
    enrollment_type = models.CharField(choices=enrollment_choices, max_length=4, default="O", blank=True, null=True)
    language = models.CharField(choices=lang_choices, max_length=4, default="E", blank=True, null=True)
    card_image = models.ImageField(upload_to=None, blank=True, null=True)
    intro_video = models.FileField(upload_to=None, blank=True, null=True)
    entrance_exam_required = models.BooleanField(blank=True, null=True)
    prerequisite = models.FileField(upload_to=None, blank=True, null=True)
    requirement_no_of_week = models.IntegerField(blank=True, null=True)
    publication_status =  models.CharField(choices=publication_choices, max_length=4, default="DN", blank=True, null=True)
    visible_to_authoring_team = models.BooleanField(blank=True, default=True, null=True)
    visible_to_student_groups = models.BooleanField(blank=True, default=False, null=True)
    learning_style = models.CharField(choices=learning_choices, max_length=2, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class CEC_TopCourse(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    course_id = models.ForeignKey(CEC_Course, on_delete=models.PROTECT, default=0)
    is_removed = models.BooleanField(blank=True, default=False)
    date_elected = models.DateTimeField(blank=True, null=True)
    date_removed = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'CEC_TopCourse'


class CEC_FeaturedCourse(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    course_id = models.ForeignKey(CEC_Course, on_delete=models.PROTECT, default=0)
    is_removed = models.BooleanField(blank=True, default=False)
    date_elected = models.DateTimeField(blank=True, null=True)
    date_removed = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'CEC_FeaturedCourse'


class CEC_NewCourse(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    course_id = models.ForeignKey(CEC_Course, on_delete=models.PROTECT, default=0)
    is_removed = models.BooleanField(blank=True, default=False)
    date_elected = models.DateTimeField(blank=True, null=True)
    date_removed = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'CEC_NewCourse'
