# Generated by Django 4.1 on 2022-08-21 05:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSRM', '0002_csrm_user_csrm_user_address_and_more'),
        ('CAT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CAT_Course_Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('A', 'ADMIN'), ('A', 'AUTHOR'), ('L', 'LEARNER')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('course_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course')),
            ],
        ),
        migrations.CreateModel(
            name='CAT_Course_Group_Member',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('group_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_course_group')),
                ('member_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_user')),
            ],
        ),
    ]
