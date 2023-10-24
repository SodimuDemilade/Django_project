# Generated by Django 4.1 on 2022-08-26 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSRM', '0002_csrm_user_csrm_user_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csrm_institution',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('M', 'Merged'), ('D', 'Deactiavted')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_user',
            name='age',
            field=models.CharField(blank=True, choices=[('<18', 'UNDER 18'), ('18-24', 'BETWEEN 18 AND 24'), ('25-34', 'BETWEEN 35 AND 44'), ('45-54', 'BETWEEN 45 AND 54'), ('55-64', 'BETWEEN 55 AND 64'), ('65-74', 'BETWEEN 65 AND 74'), ('>75', 'OLDER THAN 75')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_user',
            name='education_level',
            field=models.CharField(blank=True, choices=[('P', 'PRIMARY'), ('S', 'SECONDARY'), ('TT/D', 'TRADE TEST/DIPLOMA'), ('H/B', 'HND/BACHELORS'), ('M', 'MASTERS'), ('P', 'PHD')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_user',
            name='employment_status',
            field=models.CharField(blank=True, choices=[('S', 'STUDENT'), ('U', 'UNEMPLOYED'), ('SE', 'SELF-EMPLOYED'), ('CE', 'COMAPNY-EMPLOYED'), ('OM', 'OWNER-MANAGER')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_user',
            name='experience_level',
            field=models.CharField(blank=True, choices=[('B', 'BEGINNER'), ('I', 'INTERMEDIATE'), ('E', 'EXPERT')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_user',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('NOT', 'NOT DECLARED')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_user',
            name='language',
            field=models.CharField(choices=[('E', 'ENGLISH'), ('F', 'FRENCH'), ('C', 'CHINESE')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_user',
            name='marital_status',
            field=models.CharField(choices=[('S', 'SINGLE'), ('M', 'MARRIED'), ('D/W', 'DIVORCED/WIDOWED'), ('NOT', 'NOT DECLARED')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_user',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'ACTIVE'), ('M', 'MERGED'), ('D', 'DEACTIVATED')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_user_address',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('P', 'Previous')], max_length=4),
        ),
    ]
