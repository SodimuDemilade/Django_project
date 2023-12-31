# Generated by Django 4.1 on 2022-09-09 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSRM', '0004_rename_desciption_csrm_institution_description'),
        ('CAT', '0009_alter_cat_course_created_by_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_course',
            name='created_by_id',
            field=models.ForeignKey(blank=True, db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='CAT.cat_instructor'),
        ),
        migrations.AlterField(
            model_name='cat_course',
            name='institution_id',
            field=models.ForeignKey(blank=True, db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution'),
        ),
    ]
