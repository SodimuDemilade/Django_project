# Generated by Django 4.1 on 2022-08-19 19:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSRM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSRM_User',
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
            ],
        ),
        migrations.CreateModel(
            name='CSRM_User_Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=250)),
                ('address2', models.CharField(max_length=250, null=True)),
                ('city', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('P', 'Previous')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='csrm_institution',
            name='section_name',
        ),
        migrations.RemoveField(
            model_name='csrm_institution',
            name='subsection_name',
        ),
        migrations.AddField(
            model_name='csrm_institution',
            name='hq_town',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='lookup_country',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lookup_industry',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lookup_state',
            name='capital',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lookup_state',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='desciption',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='faceook_page',
            field=models.CharField(max_length=191, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='hq_address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='linkedin_page',
            field=models.CharField(max_length=191, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='logo',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='no_of_employers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='registration_number',
            field=models.CharField(max_length=191, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='short_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('M', 'Merged'), ('D', 'Deactiavted')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution',
            name='website',
            field=models.CharField(max_length=191, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_member',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_member',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_member',
            name='membership_designation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_member',
            name='membership_emailaddress',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_member',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_office',
            name='address1',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_office',
            name='address2',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_office',
            name='city',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_office',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_office',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_office',
            name='office_phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_office',
            name='postalcode',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_office',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_state'),
        ),
        migrations.AlterField(
            model_name='csrm_institution_office',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_section',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_section',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_section',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_subsection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_subsection',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='csrm_institution_subsection',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='lookup_country',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lookup_country',
            name='nicename',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='lookup_country',
            name='numcode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lookup_country',
            name='phonecode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lookup_country',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='lookup_industry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lookup_industry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='lookup_state',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lookup_state',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='lookup_state',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='CSRM_User_Table',
        ),
        migrations.AddField(
            model_name='csrm_user_address',
            name='country_of_resident',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_country'),
        ),
        migrations.AddField(
            model_name='csrm_user_address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_state'),
        ),
        migrations.AddField(
            model_name='csrm_user',
            name='address_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_user_address'),
        ),
        migrations.AddField(
            model_name='csrm_user',
            name='curr_employer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution'),
        ),
        migrations.AddField(
            model_name='csrm_user',
            name='curr_employer_office_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution_office'),
        ),
        migrations.AddField(
            model_name='csrm_user',
            name='industry_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_industry'),
        ),
        migrations.AddField(
            model_name='csrm_user',
            name='nationality_id',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_country'),
        ),
    ]
