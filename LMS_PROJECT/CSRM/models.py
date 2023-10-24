from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
class Lookup_Country(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=80)
    nicename = models.CharField(max_length=80,null=True)
    iso3 = models.CharField(max_length=3)
    numcode = models.IntegerField(null=True)
    phonecode = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class Lookup_State(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=30)
    capital= models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class Lookup_Industry(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CSRM_Institution(models.Model):
    stat_choices = (
        ('A', 'Active'),
        ('M', 'Merged'),
        ('D', 'Deactiavted'),
    )
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    industry_id = models.ForeignKey(Lookup_Industry, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Lookup_Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    phone = models.CharField(max_length=20, null=True)
    hq_address = models.CharField(max_length=250, null=True)
    hq_town = models.CharField(max_length=250, null=True)
    registration_number = models.CharField(max_length=191, null=True)
    logo = models.ImageField(upload_to=None, null=True)
    no_of_employers = models.IntegerField(null=True)
    linkedin_page = models.CharField(max_length=191, null=True)
    faceook_page = models.CharField(max_length=191, null=True)
    website = models.CharField(max_length=191, null=True)
    status = models.CharField(choices=stat_choices, max_length=4, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CSRM_Institution_Office(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    institution_id = models.ForeignKey(CSRM_Institution, on_delete=models.CASCADE)
    office_name = models.CharField(max_length=50)
    office_phone = models.CharField(max_length=20, null=True)
    address1 = models.CharField(max_length=250, null=True)
    address2 = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    postalcode = models.CharField(max_length=20, null=True)
    state = models.ForeignKey(Lookup_State, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class CSRM_Institution_Section(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    institution_id = models.ForeignKey(CSRM_Institution, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class CSRM_Institution_Subsection(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    institution_section_id = models.ForeignKey(CSRM_Institution_Section, on_delete=models.CASCADE)
    subsection_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class CSRM_Institution_Member(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    institution_id = models.ForeignKey(CSRM_Institution, on_delete=models.CASCADE)
    institution_section_id = models.ForeignKey(CSRM_Institution_Section, on_delete=models.CASCADE)
    institution_subsection_id = models.ForeignKey(CSRM_Institution_Subsection, on_delete=models.CASCADE)
    membership_id = models.CharField(max_length=20)
    membership_fullname = models.CharField(max_length=100)
    membership_designation = models.CharField(max_length=50, null=True)
    membership_emailaddress = models.EmailField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CSRM_User_Address(models.Model):

    stat_choices = (
        ('A', 'Active'),
        ('P', 'Previous'),
    )

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20, null=True)
    state = models.ForeignKey(Lookup_State, on_delete=models.CASCADE)
    country_of_resident = models.ForeignKey(Lookup_Country, on_delete=models.CASCADE, default=0)
    status = models.CharField(choices=stat_choices, max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CSRM_User(models.Model):
    age_choices = (
        ('<18', 'UNDER 18'),
        ('18-24', 'BETWEEN 18 AND 24'),
        ('25-34', 'BETWEEN 35 AND 44'),
        ('45-54', 'BETWEEN 45 AND 54'),
        ('55-64', 'BETWEEN 55 AND 64'),
        ('65-74', 'BETWEEN 65 AND 74'),
        ('>75', 'OLDER THAN 75'),
    )
    gender_choices = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('NOT', 'NOT DECLARED'),
    )
    emp_choices = (
        ('S', 'STUDENT'),
        ('U', 'UNEMPLOYED'),
        ('SE', 'SELF-EMPLOYED'),
        ('CE', 'COMAPNY-EMPLOYED'),
        ('OM', 'OWNER-MANAGER'),
    )
    marital_choices = (
        ('S', 'SINGLE'),
        ('M', 'MARRIED'),
        ('D/W', 'DIVORCED/WIDOWED'),
        ('NOT', 'NOT DECLARED'),
    )
    exp_choices = (
        ('B', 'BEGINNER'),
        ('I', 'INTERMEDIATE'),
        ('E', 'EXPERT'),
    )
    edu_choices = (
        ('P', 'PRIMARY'),
        ('S', 'SECONDARY'),
        ('TT/D', 'TRADE TEST/DIPLOMA'),
        ('H/B', 'HND/BACHELORS'),
        ('M', 'MASTERS'),
        ('P', 'PHD'),
    )
    lang_choices = (
        ('E', 'ENGLISH'),
        ('F', 'FRENCH'),
        ('C', 'CHINESE'),
    )
    stat_choices = (
        ('A', 'ACTIVE'),
        ('M', 'MERGED'),
        ('D', 'DEACTIVATED'),
    )

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    p_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, default='a')
    image_url = models.ImageField(upload_to=None, blank=True, null=True)
    age = models.CharField(choices=age_choices, max_length=6, blank=True, null=True)
    gender = models.CharField(choices=gender_choices, max_length=4, null=True)
    DOB = models.DateField(blank=True, null=True)
    nationality_id = models.ForeignKey(Lookup_Country, on_delete=models.CASCADE, default=0, blank=True, null=True)
    industry_id = models.ForeignKey(Lookup_Industry, on_delete=models.CASCADE, blank=True, null=True)
    address_id = models.ForeignKey(CSRM_User_Address, on_delete=models.CASCADE, blank=True, null=True)
    brief_introduction = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to=None, blank=True, null=True)
    employment_status = models.CharField(choices=emp_choices, max_length=4, blank=True, null=True)
    marital_status = models.CharField(choices=marital_choices, max_length=4, null=True)
    experience_level = models.CharField(choices=exp_choices, max_length=4, blank=True, null=True)
    education_level = models.CharField(choices=edu_choices, max_length=4, blank=True, null=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(choices=lang_choices, max_length=4, null=True)
    curr_employer = models.CharField(max_length=250, blank=True, null=True)
    curr_employer_id = models.ForeignKey(CSRM_Institution, on_delete=models.CASCADE, blank=True, null=True)
    curr_employer_office_id = models.ForeignKey(CSRM_Institution_Office, on_delete=models.CASCADE, blank=True, null=True)
    curr_employment_designation = models.CharField(max_length=191, blank=True, null=True)
    facebook_url = models.CharField(max_length=191, blank=True, null=True)
    linkedin_url = models.CharField(max_length=191, blank=True, null=True)
    twitter_url = models.CharField(max_length=191, blank=True, null=True)
    is_author = models.BooleanField(blank=True)
    is_staff = models.BooleanField(blank=True)
    is_admin = models.BooleanField(blank=True)
    status = models.CharField(choices=stat_choices, max_length=4, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    first_time_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.first_name  + " "  + self.last_name
