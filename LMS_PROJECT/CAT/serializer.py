from rest_framework import serializers
from .models import (CAT_Course, CAT_Course_Team, CAT_Course_Lesson, CAT_Course_Grading, CAT_Course_Section,CAT_Course_Question,
CAT_Course_Component, CAT_Course_Subsection, CAT_Courses_Resources, CAT_Instructor, CAT_Course_Group, CAT_Course_Group_Member)
from CSRM.serializer import CSRM_Institution_Serializer


class CAT_Course_Group_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Group
        fields = "__all__"

class CAT_Course_Group_Member_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Group_Member
        fields = "__all__"

class CAT_Instructor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Instructor
        fields = ['first_name', 'last_name', 'email']

class CAT_Course_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course
        fields = ['code', 'name', 'created_by_id']

class CAT_Course_Edit_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course
        fields = "__all__"

class CAT_All_Course_list_Serializer(serializers.ModelSerializer):
    created_by_id = CAT_Instructor_Serializer(read_only=True)
    institution_id = CSRM_Institution_Serializer(read_only=True)
    class Meta:
        model = CAT_Course
        fields = "__all__"

class CAT_Course_Team_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Team
        fields = "__all__"

class CAT_CourseLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Lesson
        fields = ['id', 'position_id', 'title']

class CAT_CourseEditLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Lesson
        fields = "__all__"

class CAT_Course_Grading_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Grading
        fields = "__all__"

class CAT_CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Section
        fields = ['id', 'position_id', 'title']

class CAT_CourseEditSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Section
        fields = "__all__"

class CAT_Course_Question_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Question
        fields = "__all__"

class CAT_CourseComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Component
        fields = ['id', 'position_id', 'type']

class CAT_CourseEditComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Component
        fields = "__all__"

class CAT_CourseSubsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Subsection
        fields = ['id', 'position_id', 'title']

class CAT_CourseEditSubsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Course_Subsection
        fields = "__all__"

class CAT_Courses_Resources_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_Courses_Resources
        fields = "__all__"
