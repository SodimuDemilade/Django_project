# Generated by Django 4.1 on 2022-09-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAT', '0006_alter_cat_course_short_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_course',
            name='course_pacing',
            field=models.CharField(blank=True, choices=[('I', 'INSTRUCTOR-LED'), ('S', 'SELF-PACED')], default='I', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='cat_course',
            name='enrollment_type',
            field=models.CharField(blank=True, choices=[('O', 'OPEN'), ('B', 'BY_INVITATION')], default='O', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='cat_course',
            name='language',
            field=models.CharField(blank=True, choices=[('E', 'ENGLISH'), ('F', 'FRENCH'), ('C', 'CHINESE'), ('Y', 'YORUBA'), ('H', 'HAUSA'), ('I', 'IGBO')], default='E', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='cat_course',
            name='level',
            field=models.CharField(blank=True, choices=[('I', 'INTRODUCTORY'), ('IN', 'INTERMEDIATE'), ('A', 'ADVANCED')], default='I', max_length=4, null=True),
        ),
    ]
