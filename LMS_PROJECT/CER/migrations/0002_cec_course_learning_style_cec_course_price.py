# Generated by Django 4.1 on 2022-09-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CER', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cec_course',
            name='learning_style',
            field=models.CharField(blank=True, choices=[('s', 'SELF PACED'), ('I', 'INSTRUCTOR LED')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='cec_course',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]