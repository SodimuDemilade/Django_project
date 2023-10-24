from django.db import models
from django.utils import timezone
import uuid
from CAT.models import CAT_Course
from CSRM.models import CSRM_Institution, CSRM_User

# Create your models here.
class LMS_Course(models.Model):

    publication_choices = (
        ('NP', 'DRAFT (NEVER PUBLISHED)'),
        ('NR', 'PUBLISHED (NOT YET RELEASED)'),
        ('PL', 'PUBLISHED AND LIVE'),
        ('UC', 'DRAFT (UNPUBLISHED CHANGES)'),
        ('AR', 'ARCHIVED'),
        ('ER', 'EXPIRED AND REPLACED'),
        ('EN', 'EXPIRED AND NOT REPLACED'),
    )

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    cat_course_id = models.ForeignKey(CAT_Course, on_delete=models.PROTECT, default=0)
    code = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=250, blank=True, null=True)
    institution_id = models.ForeignKey(CSRM_Institution, on_delete=models.PROTECT, default=0, null=True)
    visible_to_authoring_team = models.BooleanField(blank=True, default=True, null=True)
    visible_to_student_groups = models.BooleanField(blank=True, default=False, null=True)
    publication_status =  models.CharField(choices=publication_choices, max_length=2, default="NP", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'LMS_Course'

class LMS_Page(models.Model):
    page_type_choices = (
        ('SE', 'SESSION)'),
        ('SU', 'SUBSECTION)'),
        ('LE', 'LESSON'),
    )

    publication_choices = (
        ('NP', 'DRAFT (NEVER PUBLISHED)'),
        ('NR', 'PUBLISHED (NOT YET RELEASED)'),
        ('PL', 'PUBLISHED AND LIVE'),
        ('UC', 'DRAFT (UNPUBLISHED CHANGES)'),
        ('AR', 'ARCHIVED'),
        ('ER', 'EXPIRED AND REPLACED'),
        ('EN', 'EXPIRED AND NOT REPLACED'),
    )

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    course_id = models.ForeignKey(LMS_Course, on_delete=models.PROTECT, default=0)
    page_type = models.CharField(choices=page_type_choices, max_length=2, default="SE", blank=True, null=True)
    row_id = models.UUIDField(default = uuid.uuid4, editable = False)
    position_id = models.CharField(max_length=8)
    title = models.CharField(max_length=250, null=True)
    overview = models.TextField(null=True)
    component_types = models.CharField(max_length=11, null=True) #a list of types VI, IM, HT, EX separated by commas
    rights_ro = models.CharField(max_length=250, null=True)
    rights_none = models.CharField(max_length=250, null=True)
    publication_status =  models.CharField(choices=publication_choices, max_length=2, default="NP", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'LMS_Page'
        ordering = ['position_id']


class LMS_Component(models.Model):
    type_choices=(
        ('VI', 'VIDEO'),
        ('IM', 'IMAGE'),
        ('HT', 'HTML'),
        ('EX', 'EXERCISE'),
    )
    video_choices=(
        ('VI', 'VIMEO'),
        ('YO', 'YOUTUBE'),
        ('MP', 'MP4'),
        ('WZ', 'WEBINAR ON ZOOM'),
        ('ME', 'MEETING ON ZOOM'),
        ('WV', 'WEBINAR ON VIMEO'),
    )
    html_choices=(
        ('HT', 'HTML'),
        ('IF', 'IFRAME'),
    )
    exercise_type_choices=(
        ('QI', 'QUIZ'),
        ('ON', 'ONLINETEST'),
        ('OF', 'OFFLINETEST'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    page_id = models.ForeignKey(LMS_Page, null=False, on_delete=models.PROTECT, default=0)
    position_id = models.CharField(max_length=11, null=False)
    type = models.CharField(choices=type_choices, max_length=2)
    video_type = models.CharField(choices=video_choices, max_length=2, null=True)
    video_header = models.CharField(max_length=250, null=True)
    video_footer = models.CharField(max_length=250, null=True)
    recorded_url = models.CharField(max_length=250, null=True)
    live_url = models.CharField(max_length=250, null=True)
    mobile_url = models.CharField(max_length=250, null=True)
    starting_date_time = models.CharField(max_length=250, null=True)
    image_header = models.CharField(max_length=250, null=True)
    image_footer = models.CharField(max_length=250, null=True)
    image_url = models.URLField(null=True)
    html_title = models.CharField(max_length=250, null=True)
    html_type = models.CharField(choices=html_choices, max_length=2, null=True)
    html_content = models.TextField(null=True)
    html_url = models.CharField(max_length=250, null=True)
    exercise_type = models.CharField(choices=exercise_type_choices, max_length=2, null=True)
    grading_weight = models.IntegerField(default=0, null=True)
    total_score = models.IntegerField(null=True)
    available_date_time = models.DateTimeField(null=True)
    start_date_time = models.DateTimeField(null=True)
    duration = models.IntegerField(null=True)
    due_date_time = models.DateTimeField(null=True)
    show_allocated_score = models.BooleanField(null=True)
    show_hint = models.BooleanField(null=True)
    show_answer = models.BooleanField(null=True)
    exercise_overview = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'LMS_Component'


class LMS_Question(models.Model):
    type_choices=(
        ('TE', 'TEXT'),
        ('NU', 'NUMBER'),
        ('RA', 'RADIOBUTTON'),
        ('CH', 'CHECKBOX'),
        ('DR', 'DROPDOWN'),
        ('ES', 'ESSAY'),
        ('DI', 'DISCUSSION'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    component_id = models.ForeignKey(LMS_Component, on_delete=models.PROTECT, default=0)
    question_no = models.IntegerField()
    type = models.CharField(choices=type_choices, max_length=2)
    question = models.FileField(upload_to=None)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    option5 = models.CharField(max_length=250)
    answer_text = models.CharField(max_length=250)
    answer_number = models.CharField(max_length=250)
    answer_options = models.CharField(max_length=10)
    hint = models.FileField(upload_to=None)
    feedback = models.FileField(upload_to=None)
    allocated_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'LMS_Question'


class LMS_Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    user_id = models.ForeignKey(CSRM_User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(LMS_Course, on_delete=models.CASCADE)
    completed_position_id = models.TextField(null=True)
    enrollment_status =  models.CharField(max_length=100, null=True)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return " {}  is enrolled for {}".format(self.user, self.course)

class LMS_BookmarkComment(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    enrolment_id = models.ForeignKey(LMS_Enrollment, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    bookmarked = models.BooleanField(default=False, null=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return "{} Bookmark  by {} ".format(self.course.name, self.user)
