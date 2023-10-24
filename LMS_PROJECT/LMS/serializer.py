from rest_framework import serializers
from .models import (LMS_Course, LMS_Page, LMS_Question, LMS_Component, LMS_Enrollment, LMS_BookmarkComment)
from CSRM.serializer import CSRM_Institution_Serializer


class LMS_CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LMS_Course
        fields = "__all__"

class LMS_PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LMS_Page
        fields = ['id', 'page_type', 'title', 'position_id']


class LMS_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LMS_Question
        fields = "__all__"

class LMS_ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LMS_Component
        fields = ['id', 'page_id', 'position_id', 'type']

class LMS_EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LMS_Enrollment
        fields = "__all__"

class LMS_BookmarkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LMS_BookmarkComment
        fields = "__all__"
