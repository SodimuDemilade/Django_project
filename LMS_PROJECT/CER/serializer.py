from rest_framework import serializers
from .models import (CEC_Course, CEC_TopCourse, CEC_FeaturedCourse, CEC_NewCourse)



class CEC_CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CEC_Course
        fields = "__all__"
