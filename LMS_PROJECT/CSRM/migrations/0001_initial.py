# Generated by Django 4.1 on 2022-08-16 01:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSRM_Institution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=10)),
                ('desciption', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('hq_address', models.CharField(max_length=250)),
                ('registration_number', models.CharField(max_length=191)),
                ('logo', models.ImageField(upload_to=None)),
                ('no_of_employers', models.IntegerField()),
                ('section_name', models.CharField(max_length=100)),
                ('subsection_name', models.CharField(max_length=100)),
                ('linkedin_page', models.CharField(max_length=191)),
                ('faceook_page', models.CharField(max_length=191)),
                ('website', models.CharField(max_length=191)),
                ('status', models.CharField(choices=[('A', 'Active'), ('M', 'Merged'), ('D', 'Deactiavted')], max_length=20)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CSRM_Institution_Office',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('office_name', models.CharField(max_length=50)),
                ('office_phone', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=250)),
                ('address2', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('postalcode', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
                ('institution_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution')),
            ],
        ),
        migrations.CreateModel(
            name='CSRM_Institution_Section',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('section_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
                ('institution_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution')),
            ],
        ),
        migrations.CreateModel(
            name='Lookup_Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('iso', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=80)),
                ('nicename', models.CharField(max_length=80)),
                ('iso3', models.CharField(max_length=3)),
                ('numcode', models.IntegerField(max_length=6)),
                ('phonecode', models.IntegerField(max_length=11)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Lookup_Industry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=191)),
                ('description', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Lookup_State',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CSRM_User_Table',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('p_number', models.CharField(max_length=20)),
                ('password', models.CharField(default='a', max_length=20)),
                ('image_url', models.ImageField(upload_to=None)),
                ('age', models.CharField(choices=[('<18', 'Under 18'), ('18-24', 'Between 18 and 24'), ('25-34', 'Between 35 and 44'), ('45-54', 'Between 45 and 54'), ('55-64', 'Between 55 and 64'), ('65-74', 'Between 65 and 74'), ('>75', 'Older than 75')], max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('DOB', models.DateField()),
                ('address2', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=250)),
                ('brief_introduction', models.TextField()),
                ('resume', models.FileField(upload_to=None)),
                ('employment_status', models.CharField(choices=[('S', 'Student'), ('U', 'Unemployed'), ('Se', 'Self-Employed'), ('CE', 'Comapny-Employed'), ('OM', 'Owner-Manager')], max_length=20)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D/W', 'Divorced/Widowed')], max_length=20)),
                ('experience_level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('E', 'Expert')], max_length=20)),
                ('education_level', models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary'), ('TT/D', 'Trade Test/Diploma'), ('H/B', 'HND/Bachelors'), ('M', 'Masters'), ('P', 'PHD')], max_length=20)),
                ('degree', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[('E', 'English'), ('F', 'French'), ('C', 'Chinese')], max_length=20)),
                ('curr_employment_designation', models.CharField(max_length=191)),
                ('facebook_url', models.CharField(max_length=191)),
                ('linkedin_url', models.CharField(max_length=191)),
                ('twitter_url', models.CharField(max_length=191)),
                ('is_author', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('is_admin', models.BooleanField()),
                ('status', models.CharField(choices=[('A', 'Active'), ('M', 'Merged'), ('D', 'Deactiavted')], max_length=20)),
                ('email_verified_at', models.DateTimeField()),
                ('first_time_login', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
                ('country_of_resident', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='country_of_resident', to='CSRM.lookup_country')),
                ('curr_employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution')),
                ('curr_employer_office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution_office')),
                ('industry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_industry')),
                ('nationality', models.ManyToManyField(default=0, related_name='nationality', to='CSRM.lookup_country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_state')),
            ],
        ),
        migrations.CreateModel(
            name='CSRM_Institution_Subsection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subsection_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
                ('institution_section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution_section')),
            ],
        ),
        migrations.AddField(
            model_name='csrm_institution_office',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_state'),
        ),
        migrations.CreateModel(
            name='CSRM_Institution_Member',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('membership_id', models.CharField(max_length=20)),
                ('membership_fullname', models.CharField(max_length=100)),
                ('membership_designation', models.CharField(max_length=50)),
                ('membership_emailaddress', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
                ('institution_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution')),
                ('institution_section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution_section')),
                ('institution_subsection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.csrm_institution_subsection')),
            ],
        ),
        migrations.AddField(
            model_name='csrm_institution',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_country'),
        ),
        migrations.AddField(
            model_name='csrm_institution',
            name='industry_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSRM.lookup_industry'),
        ),
    ]
