# Generated by Django 4.1 on 2022-08-19 19:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CSRM', '0002_csrm_user_csrm_user_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CAT_Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('version', models.IntegerField(null=True)),
                ('semester', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('short_description', models.CharField(max_length=250, null=True)),
                ('overview', models.FileField(blank=True, null=True, upload_to=None)),
                ('level', models.CharField(choices=[('I', 'INTRODUCTORY'), ('IN', 'INTERMEDIATE'), ('A', 'ADVANCED')], default='INTRODUCTORY', max_length=50)),
                ('course_pacing', models.CharField(choices=[('I', 'INSTRUCTOR-LED'), ('S', 'SELF-PACED')], default='INSTRUCTOR-LED', max_length=50)),
                ('enrollment_type', models.CharField(choices=[('O', 'OPEN'), ('B', 'BY_INVITATION')], default='OPEN', max_length=50)),
                ('language', models.CharField(choices=[('E', 'ENGLISH'), ('F', 'FRENCH'), ('C', 'CHINESE'), ('Y', 'YORUBA'), ('H', 'HAUSA'), ('I', 'IGBO')], default='ENGLISH', max_length=50)),
                ('card_image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('intro_video', models.FileField(blank=True, null=True, upload_to=None)),
                ('entrance_exam_required', models.BooleanField(blank=True, null=True)),
                ('prerequisite', models.FileField(blank=True, null=True, upload_to=None)),
                ('requirement_no_of_week', models.IntegerField(blank=True, null=True)),
                ('publication_status', models.CharField(blank=True, choices=[('D', 'DRAFT(NEVER PUBLISHED)'), ('P', 'PUBLISHED(NOT YET RELEASED)'), ('PL', 'PUBLISHED AND LIVE'), ('D', 'DRAFT(UNPUBLISHED CHANGES)')], default='DRAFT(NEVER PUBLISHED)', max_length=50, null=True)),
                ('visible_to_authoring_team', models.BooleanField(blank=True, default=True)),
                ('visible_to_student_groups', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Course_Component',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position_id', models.CharField(max_length=11)),
                ('type', models.CharField(choices=[('V', 'VIDEO'), ('I', 'IMAGE'), ('H', 'HTML'), ('E', 'EXERCISE')], max_length=10)),
                ('video_type', models.CharField(choices=[('V', 'VIMEO'), ('Y', 'YOUTUBE'), ('M', 'MP4'), ('WZ', 'WEBINAR ON ZOOM'), ('ME', 'MEETING ON ZOOM'), ('WV', 'WEBINAR ON VIMEO')], max_length=20, null=True)),
                ('video_header', models.CharField(max_length=250, null=True)),
                ('video_footer', models.CharField(max_length=250, null=True)),
                ('recorded_url', models.CharField(max_length=250, null=True)),
                ('live_url', models.CharField(max_length=250, null=True)),
                ('mobile_url', models.CharField(max_length=250, null=True)),
                ('starting_date_time', models.CharField(max_length=250, null=True)),
                ('image_header', models.CharField(max_length=250, null=True)),
                ('image_footer', models.CharField(max_length=250, null=True)),
                ('image_url', models.URLField(null=True)),
                ('html_title', models.CharField(max_length=250, null=True)),
                ('html_type', models.CharField(choices=[('H', 'HTML'), ('I', 'IFRAME')], max_length=10, null=True)),
                ('html_content', models.TextField(null=True)),
                ('html_url', models.CharField(max_length=250, null=True)),
                ('exercise_type', models.CharField(choices=[('V', 'QUIZ'), ('Y', 'ONLINETEST'), ('M', 'OFFLINETEST')], max_length=20, null=True)),
                ('grading_weight', models.IntegerField(default=0, null=True)),
                ('total_score', models.IntegerField(null=True)),
                ('available_date_time', models.DateTimeField(null=True)),
                ('start_date_time', models.DateTimeField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('due_date_time', models.DateTimeField(null=True)),
                ('show_allocated_score', models.BooleanField(null=True)),
                ('show_hint', models.BooleanField(null=True)),
                ('show_answer', models.BooleanField(null=True)),
                ('exercise_overview', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Course_Section',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position_id', models.CharField(max_length=2)),
                ('title', models.CharField(max_length=250)),
                ('overview', models.TextField(null=True)),
                ('rights', models.CharField(default='RW', max_length=4)),
                ('publication_status', models.CharField(blank=True, choices=[('D', 'DRAFT(NEVER PUBLISHED)'), ('P', 'PUBLISHED(NOT YET RELEASED)'), ('PL', 'PUBLISHED AND LIVE'), ('D', 'DRAFT(UNPUBLISHED CHANGES)')], default='DRAFT(NEVER PUBLISHED)', max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course')),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Instructor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('p_number', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(default='a', max_length=20)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=None)),
                ('age', models.CharField(blank=True, choices=[('<18', 'UNDER 18'), ('18-24', 'BETWEEN 18 AND 24'), ('25-34', 'BETWEEN 35 AND 44'), ('45-54', 'BETWEEN 45 AND 54'), ('55-64', 'BETWEEN 55 AND 64'), ('65-74', 'BETWEEN 65 AND 74'), ('>75', 'OLDER THAN 75')], max_length=20, null=True)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('NOT', 'NOT DECLARED')], max_length=20, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('brief_introduction', models.TextField(blank=True, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to=None)),
                ('employment_status', models.CharField(blank=True, choices=[('S', 'STUDENT'), ('U', 'UNEMPLOYED'), ('SE', 'SELF-EMPLOYED'), ('CE', 'COMAPNY-EMPLOYED'), ('OM', 'OWNER-MANAGER')], max_length=20, null=True)),
                ('marital_status', models.CharField(choices=[('S', 'SINGLE'), ('M', 'MARRIED'), ('D/W', 'DIVORCED/WIDOWED'), ('NOT', 'NOT DECLARED')], max_length=20, null=True)),
                ('experience_level', models.CharField(blank=True, choices=[('B', 'BEGINNER'), ('I', 'INTERMEDIATE'), ('E', 'EXPERT')], max_length=20, null=True)),
                ('education_level', models.CharField(blank=True, choices=[('P', 'PRIMARY'), ('S', 'SECONDARY'), ('TT/D', 'TRADE TEST/DIPLOMA'), ('H/B', 'HND/BACHELORS'), ('M', 'MASTERS'), ('P', 'PHD')], max_length=20, null=True)),
                ('degree', models.CharField(blank=True, max_length=50, null=True)),
                ('language', models.CharField(choices=[('E', 'ENGLISH'), ('F', 'FRENCH'), ('C', 'CHINESE')], max_length=20, null=True)),
                ('curr_employer', models.CharField(blank=True, max_length=250, null=True)),
                ('curr_employment_designation', models.CharField(blank=True, max_length=191, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=191, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=191, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=191, null=True)),
                ('is_author', models.BooleanField(blank=True)),
                ('is_staff', models.BooleanField(blank=True)),
                ('is_admin', models.BooleanField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('A', 'ACTIVE'), ('M', 'MERGED'), ('D', 'DEACTIVATED')], max_length=20, null=True)),
                ('email_verified_at', models.DateTimeField(blank=True, null=True)),
                ('first_time_login', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('address_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_user_address')),
                ('curr_employer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution')),
                ('curr_employer_office_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution_office')),
                ('industry_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_industry')),
                ('nationality_id', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_country')),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Courses_Resources',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('I', 'IMAGE'), ('V', 'VIDEO'), ('H', 'HTML'), ('P', 'PDF'), ('W', 'WORD'), ('E', 'EXCEL'), ('PP', 'POWERPOINT'), ('O', 'OTHERS')], max_length=50)),
                ('file_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course')),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Course_Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('S', 'STAFF'), ('L', 'LEAD'), ('A', 'AUTHOR'), ('R', 'READER')], default='LEAD', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course')),
                ('member_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_instructor')),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Course_Subsection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position_id', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=250)),
                ('overview', models.TextField(null=True)),
                ('rights', models.CharField(default='RW', max_length=4)),
                ('publication_status', models.CharField(blank=True, choices=[('D', 'DRAFT(NEVER PUBLISHED)'), ('P', 'PUBLISHED(NOT YET RELEASED)'), ('PL', 'PUBLISHED AND LIVE'), ('D', 'DRAFT(UNPUBLISHED CHANGES)')], default='DRAFT(NEVER PUBLISHED)', max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('section_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course_section')),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Course_Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question_no', models.IntegerField()),
                ('type', models.CharField(choices=[('T', 'TEXT'), ('N', 'NUMBER'), ('R', 'RADIOBUTTON'), ('C', 'CHECKBOX'), ('DR', 'DROPDOWN'), ('E', 'ESSAY'), ('D', 'DISCUSSION')], max_length=50)),
                ('question', models.FileField(upload_to=None)),
                ('option1', models.CharField(max_length=255)),
                ('option2', models.CharField(max_length=255)),
                ('option3', models.CharField(max_length=255)),
                ('option4', models.CharField(max_length=255)),
                ('option5', models.CharField(max_length=255)),
                ('answer_text', models.CharField(max_length=255)),
                ('answer_number', models.CharField(max_length=255)),
                ('answer_options', models.CharField(max_length=10)),
                ('hint', models.FileField(upload_to=None)),
                ('feedback', models.FileField(upload_to=None)),
                ('allocated_score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('component_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course_component')),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Course_Lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position_id', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=250)),
                ('overview', models.TextField(null=True)),
                ('rights', models.CharField(default='RW', max_length=4)),
                ('publication_status', models.CharField(blank=True, choices=[('D', 'DRAFT(NEVER PUBLISHED)'), ('P', 'PUBLISHED(NOT YET RELEASED)'), ('PL', 'PUBLISHED AND LIVE'), ('D', 'DRAFT(UNPUBLISHED CHANGES)')], default='DRAFT(NEVER PUBLISHED)', max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('subsection_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course_subsection')),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Course_Grading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grade_letter', models.CharField(max_length=2)),
                ('grade_description', models.CharField(max_length=20)),
                ('upper_bound', models.IntegerField()),
                ('lower_bound', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course')),
            ],
        ),
        migrations.AddField(
            model_name='cat_course_component',
            name='lesson_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course_lesson'),
        ),
        migrations.AddField(
            model_name='cat_course',
            name='created_by_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_instructor'),
        ),
        migrations.AddField(
            model_name='cat_course',
            name='institution_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution'),
        ),
    ]
