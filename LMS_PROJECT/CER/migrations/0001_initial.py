# Generated by Django 4.1 on 2022-09-11 02:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CAT', '0011_alter_cat_course_created_by_id_and_more'),
        ('CSRM', '0004_rename_desciption_csrm_institution_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CEC_Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('semester', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('short_description', models.CharField(blank=True, max_length=250, null=True)),
                ('overview', models.FileField(blank=True, null=True, upload_to=None)),
                ('level', models.CharField(blank=True, choices=[('I', 'INTRODUCTORY'), ('IN', 'INTERMEDIATE'), ('A', 'ADVANCED')], default='I', max_length=4, null=True)),
                ('course_pacing', models.CharField(blank=True, choices=[('I', 'INSTRUCTOR-LED'), ('S', 'SELF-PACED')], default='I', max_length=4, null=True)),
                ('enrollment_type', models.CharField(blank=True, choices=[('O', 'OPEN'), ('B', 'BY_INVITATION')], default='O', max_length=4, null=True)),
                ('language', models.CharField(blank=True, choices=[('E', 'ENGLISH'), ('F', 'FRENCH'), ('C', 'CHINESE'), ('Y', 'YORUBA'), ('H', 'HAUSA'), ('I', 'IGBO')], default='E', max_length=4, null=True)),
                ('card_image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('intro_video', models.FileField(blank=True, null=True, upload_to=None)),
                ('entrance_exam_required', models.BooleanField(blank=True, null=True)),
                ('prerequisite', models.FileField(blank=True, null=True, upload_to=None)),
                ('requirement_no_of_week', models.IntegerField(blank=True, null=True)),
                ('publication_status', models.CharField(blank=True, choices=[('DN', 'DRAFT(NEVER PUBLISHED)'), ('P', 'PUBLISHED(NOT YET RELEASED)'), ('PL', 'PUBLISHED AND LIVE'), ('DU', 'DRAFT(UNPUBLISHED CHANGES)')], default='DN', max_length=4, null=True)),
                ('visible_to_authoring_team', models.BooleanField(blank=True, default=True, null=True)),
                ('visible_to_student_groups', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_instructor')),
                ('institution_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution')),
            ],
        ),
        migrations.CreateModel(
            name='CEC_TopCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_removed', models.BooleanField(blank=True, default=False)),
                ('date_elected', models.DateTimeField(blank=True, null=True)),
                ('date_removed', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='CER.cec_course')),
            ],
            options={
                'db_table': 'CEC_TopCourse',
            },
        ),
        migrations.CreateModel(
            name='CEC_NewCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_removed', models.BooleanField(blank=True, default=False)),
                ('date_elected', models.DateTimeField(blank=True, null=True)),
                ('date_removed', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='CER.cec_course')),
            ],
            options={
                'db_table': 'CEC_NewCourse',
            },
        ),
        migrations.CreateModel(
            name='CEC_FeaturedCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_removed', models.BooleanField(blank=True, default=False)),
                ('date_elected', models.DateTimeField(blank=True, null=True)),
                ('date_removed', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='CER.cec_course')),
            ],
            options={
                'db_table': 'CEC_FeaturedCourse',
            },
        ),
    ]
