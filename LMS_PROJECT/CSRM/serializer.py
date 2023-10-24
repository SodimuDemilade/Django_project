from rest_framework import serializers
from .models import (Lookup_State, Lookup_Country, Lookup_Industry, CSRM_Institution, CSRM_Institution_Office,
CSRM_Institution_Section, CSRM_Institution_Subsection, CSRM_Institution_Member, CSRM_User, CSRM_User_Address)


class CSRM_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CSRM_User
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'email', 'p_number', 'password',
        'image_url' 'age', 'gender', 'DOB', 'nationality_id', 'industry_id', 'address_id', 'brief_introduction'
        'resume', 'employment_status', 'marital_status', 'experience_level', 'education_level',
        'degree', 'language', 'curr_employer', 'curr_employer_id', 'curr_employer_id', 'curr_employer_office_id',
        'curr_employment_designation', 'facebook_url', 'linkedin_url', 'twitter_url', 'is_author', 'is_staff', 'is_admin',
        'status', 'email_verified_at', 'first_time_login', 'created_at', 'updated_at', 'deleted_at']

class CSRM_User_Address_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CSRM_User_Address
        fields = ['id', 'address1', 'address2', 'city', 'postalcode', 'state', 'country_of_resident', 'status',
        'created_at', 'updated_at', 'deleted_at']

class CSRM_Institution_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CSRM_Institution
        fields = ['id', 'industry_id', 'country_id', 'name', 'description',
        'phone', 'hq_address', 'hq_town', 'registration_number', 'logo',
        'no_of_employers', 'linkedin_page', 'faceook_page', 'website', 'status',
        'created_at', 'updated_at', 'deleted_at']

class CSRM_Institution_Member_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CSRM_Institution_Member
        fields = ['id', 'institution_id', 'institution_section_id', 'institution_subsection_id',
        'membership_id', 'membership_fullname', 'membership_designation', 'membership_emailaddress',
        'created_at', 'updated_at', 'deleted_at']

class CSRM_Institution_Office_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CSRM_Institution_Member
        fields = ['id', 'institution_id', 'office_name', 'office_phone', 'address1',
        'address2', 'city', 'postalcode', 'state', 'created_at', 'updated_at',
        'deleted_at']

class CSRM_Institution_Section_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CSRM_Institution_Section
        fields = ['id', 'institution_id', 'section_name', 'created_at',
        'updated_at', 'deleted_at']

class CSRM_Institution_Subsection_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CSRM_Institution_Subsection
        fields = ['id', 'institution_section_id', 'subsection_name', 'created_at',
        'updated_at', 'deleted_at']

class Lookup_State_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lookup_State
        fields = "__all__"

class Lookup_Country_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lookup_Country
        fields = ['id', 'name', 'capital', 'created_at', 'updated_at', 'deleted_at']

class Lookup_Industry_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lookup_Industry
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'deleted_at']
