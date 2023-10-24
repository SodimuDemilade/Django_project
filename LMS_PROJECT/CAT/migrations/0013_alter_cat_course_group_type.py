# Generated by Django 4.1 on 2022-09-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAT', '0012_alter_cat_course_group_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_course_group',
            name='type',
            field=models.CharField(choices=[('LA', 'LEAD AUTHOR'), ('AU', 'AUTHOR'), ('L', 'LEARNER')], max_length=4),
        ),
    ]