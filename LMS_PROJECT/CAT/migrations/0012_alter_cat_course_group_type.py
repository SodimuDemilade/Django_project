# Generated by Django 4.1 on 2022-09-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAT', '0011_alter_cat_course_created_by_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_course_group',
            name='type',
            field=models.CharField(choices=[('LE', 'LEAD AUTHOR'), ('AU', 'AUTHOR'), ('L', 'LEARNER')], max_length=4),
        ),
    ]
