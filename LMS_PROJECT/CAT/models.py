from django.db import models
from CSRM.models import CSRM_Institution, CSRM_Institution_Office, CSRM_User, CSRM_User_Address, Lookup_Industry, Lookup_Country
import uuid


# Create your models here.
class CAT_Instructor(models.Model):
    age_choices = (
        ('<18', 'UNDER 18'),
        ('18-24', 'BETWEEN 18 AND 24'),
        ('25-34', 'BETWEEN 35 AND 44'),
        ('45-54', 'BETWEEN 45 AND 54'),
        ('55-64', 'BETWEEN 55 AND 64'),
        ('65-74', 'BETWEEN 65 AND 74'),
        ('>75', 'OLDER THAN 75'),
    )
    gender_choices = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('NOT', 'NOT DECLARED'),
    )
    emp_choices = (
        ('S', 'STUDENT'),
        ('U', 'UNEMPLOYED'),
        ('SE', 'SELF-EMPLOYED'),
        ('CE', 'COMAPNY-EMPLOYED'),
        ('OM', 'OWNER-MANAGER'),
    )
    marital_choices = (
        ('S', 'SINGLE'),
        ('M', 'MARRIED'),
        ('D/W', 'DIVORCED/WIDOWED'),
        ('NOT', 'NOT DECLARED'),
    )
    exp_choices = (
        ('B', 'BEGINNER'),
        ('I', 'INTERMEDIATE'),
        ('E', 'EXPERT'),
    )
    edu_choices = (
        ('P', 'PRIMARY'),
        ('S', 'SECONDARY'),
        ('TT/D', 'TRADE TEST/DIPLOMA'),
        ('H/B', 'HND/BACHELORS'),
        ('M', 'MASTERS'),
        ('P', 'PHD'),
    )
    lang_choices = (
        ('E', 'ENGLISH'),
        ('F', 'FRENCH'),
        ('C', 'CHINESE'),
    )
    stat_choices = (
        ('A', 'ACTIVE'),
        ('M', 'MERGED'),
        ('D', 'DEACTIVATED'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    p_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, default='a')
    image_url = models.ImageField(upload_to=None, blank=True, null=True)
    age = models.CharField(choices=age_choices, max_length=6, blank=True, null=True)
    gender = models.CharField(choices=gender_choices, max_length=4, null=True)
    DOB = models.DateField(blank=True, null=True)
    nationality_id = models.ForeignKey(Lookup_Country, on_delete=models.CASCADE, default=0, blank=True, null=True)
    industry_id = models.ForeignKey(Lookup_Industry, on_delete=models.CASCADE, blank=True, null=True)
    address_id = models.ForeignKey(CSRM_User_Address, on_delete=models.CASCADE, blank=True, null=True)
    brief_introduction = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to=None, blank=True, null=True)
    employment_status = models.CharField(choices=emp_choices, max_length=4, blank=True, null=True)
    marital_status = models.CharField(choices=marital_choices, max_length=4, null=True)
    experience_level = models.CharField(choices=exp_choices, max_length=4, blank=True, null=True)
    education_level = models.CharField(choices=edu_choices, max_length=20, blank=True, null=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(choices=lang_choices, max_length=4, null=True)
    curr_employer = models.CharField(max_length=250, blank=True, null=True)
    curr_employer_id = models.ForeignKey(CSRM_Institution, on_delete=models.CASCADE, blank=True, null=True)
    curr_employer_office_id = models.ForeignKey(CSRM_Institution_Office, on_delete=models.CASCADE, blank=True, null=True)
    curr_employment_designation = models.CharField(max_length=191, blank=True, null=True)
    facebook_url = models.CharField(max_length=191, blank=True, null=True)
    linkedin_url = models.CharField(max_length=191, blank=True, null=True)
    twitter_url = models.CharField(max_length=191, blank=True, null=True)
    is_author = models.BooleanField(blank=True)
    is_staff = models.BooleanField(blank=True)
    is_admin = models.BooleanField(blank=True)
    status = models.CharField(choices=stat_choices, max_length=4, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    first_time_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.first_name  + " "  + self.last_name


class CAT_Course(models.Model):

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
        ('I', 'IGBO'),
    )

    publication_choices = (
        ('DN', 'DRAFT(NEVER PUBLISHED)'),
        ('P', 'PUBLISHED(NOT YET RELEASED)'),
        ('PL', 'PUBLISHED AND LIVE'),
        ('DU', 'DRAFT(UNPUBLISHED CHANGES)'),
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CAT_Course_Group(models.Model):
    type_choices=(
        ('LA', 'LEAD AUTHOR'),
        ('AU', 'AUTHOR'),
        ('L', 'LEARNER'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    course_id = models.ForeignKey(CAT_Course, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=50)
    type = models.CharField(choices=type_choices, max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class CAT_Course_Group_Member(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    group_id = models.ForeignKey(CAT_Course_Group, on_delete=models.CASCADE, default=0)
    member_id = models.ForeignKey(CSRM_User, on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CAT_Course_Grading(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    course_id = models.ForeignKey(CAT_Course, on_delete=models.CASCADE, default=0)
    grade_letter = models.CharField(max_length=2)
    grade_description = models.CharField(max_length=20)
    upper_bound = models.IntegerField()
    lower_bound = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class CAT_Course_Team(models.Model):
    role_choices=(
        ('S', 'STAFF'),
        ('L', 'LEAD'),
        ('A', 'AUTHOR'),
        ('R', 'READER'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    course_id = models.ForeignKey(CAT_Course, on_delete=models.CASCADE, default=0)
    member_id = models.ForeignKey(CAT_Instructor, on_delete=models.CASCADE, default=0)
    role = models.CharField(choices=role_choices, max_length=4, default='L')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CAT_Courses_Resources(models.Model):
    type_choices=(
        ('I', 'IMAGE'),
        ('V', 'VIDEO'),
        ('H', 'HTML'),
        ('P', 'PDF'),
        ('W', 'WORD'),
        ('E', 'EXCEL'),
        ('PP', 'POWERPOINT'),
        ('O', 'OTHERS'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    course_id = models.ForeignKey(CAT_Course, on_delete=models.CASCADE, default=0)
    type = models.CharField(choices=type_choices, max_length=4)
    file_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CAT_Course_Section(models.Model):
    publication_choices = (
        ('DN', 'DRAFT(NEVER PUBLISHED)'),
        ('P', 'PUBLISHED(NOT YET RELEASED)'),
        ('PL', 'PUBLISHED AND LIVE'),
        ('DU', 'DRAFT(UNPUBLISHED CHANGES)'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    course_id = models.ForeignKey(CAT_Course, on_delete=models.CASCADE, default=0)
    position_id = models.CharField(max_length=2)
    title = models.CharField(max_length=250)
    overview = models.TextField(null=True)
    rights = models.CharField(max_length=4, default="RW") #RW,RO, NONE
    publication_status =  models.CharField(choices=publication_choices, max_length=4, default="DN", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CAT_Course_Subsection(models.Model):
    publication_choices = (
        ('DN', 'DRAFT(NEVER PUBLISHED)'),
        ('P', 'PUBLISHED(NOT YET RELEASED)'),
        ('PL', 'PUBLISHED AND LIVE'),
        ('DU', 'DRAFT(UNPUBLISHED CHANGES)'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    section_id = models.ForeignKey(CAT_Course_Section, null=False, on_delete=models.CASCADE, default=0)
    position_id = models.CharField(max_length=5, null=False)
    title = models.CharField(max_length=250)
    overview = models.TextField(null=True)
    rights = models.CharField(max_length=4, default="RW") #RW,RO, NONE
    publication_status =  models.CharField(choices=publication_choices, max_length=4, default="DN", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)




class CAT_Course_Lesson(models.Model):
    publication_choices = (
        ('DN', 'DRAFT(NEVER PUBLISHED)'),
        ('P', 'PUBLISHED(NOT YET RELEASED)'),
        ('PL', 'PUBLISHED AND LIVE'),
        ('DU', 'DRAFT(UNPUBLISHED CHANGES)'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    subsection_id = models.ForeignKey(CAT_Course_Subsection, null=False, on_delete=models.CASCADE, default=0)
    position_id = models.CharField(max_length=8, null=False)
    title = models.CharField(max_length=250)
    overview = models.TextField(null=True)
    rights = models.CharField(max_length=4, default="RW") #RW,RO, NONE
    publication_status =  models.CharField(choices=publication_choices, max_length=4, default="DN", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class CAT_Course_Component(models.Model):
    type_choices=(
        ('V', 'VIDEO'),
        ('I', 'IMAGE'),
        ('H', 'HTML'),
        ('E', 'EXERCISE'),
    )
    video_choices=(
        ('V', 'VIMEO'),
        ('Y', 'YOUTUBE'),
        ('M', 'MP4'),
        ('WZ', 'WEBINAR ON ZOOM'),
        ('ME', 'MEETING ON ZOOM'),
        ('WV', 'WEBINAR ON VIMEO'),
    )
    html_choices=(
        ('H', 'HTML'),
        ('I', 'IFRAME'),
    )
    exercise_type_choices=(
        ('V', 'QUIZ'),
        ('Y', 'ONLINETEST'),
        ('M', 'OFFLINETEST'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    lesson_id = models.ForeignKey(CAT_Course_Lesson, null=False, on_delete=models.CASCADE, default=0)
    position_id = models.CharField(max_length=11, null=False)
    type = models.CharField(choices=type_choices, max_length=4)
    video_type = models.CharField(choices=video_choices, max_length=4, null=True)
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
    html_type = models.CharField(choices=html_choices, max_length=4, null=True)
    html_content = models.TextField(null=True)
    html_url = models.CharField(max_length=250, null=True)
    exercise_type = models.CharField(choices=exercise_type_choices, max_length=4, null=True)
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


class CAT_Course_Question(models.Model):
    type_choices=(
        ('T', 'TEXT'),
        ('N', 'NUMBER'),
        ('R', 'RADIOBUTTON'),
        ('C', 'CHECKBOX'),
        ('DR', 'DROPDOWN'),
        ('E', 'ESSAY'),
        ('D', 'DISCUSSION'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    component_id = models.ForeignKey(CAT_Course_Component, on_delete=models.CASCADE, default=0)
    question_no = models.IntegerField()
    type = models.CharField(choices=type_choices, max_length=4)
    question = models.FileField(upload_to=None)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    option5 = models.CharField(max_length=255)
    answer_text = models.CharField(max_length=255)
    answer_number = models.CharField(max_length=255)
    answer_options = models.CharField(max_length=10)
    hint = models.FileField(upload_to=None)
    feedback = models.FileField(upload_to=None)
    allocated_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
