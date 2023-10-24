from rest_framework.views import APIView
from .serializer import (LMS_CourseSerializer, LMS_PageSerializer, LMS_QuestionSerializer, LMS_ComponentSerializer,
LMS_EnrollmentSerializer, LMS_BookmarkCommentSerializer)
from .models import (LMS_Course, LMS_Page, LMS_Question, LMS_Component, LMS_Enrollment, LMS_BookmarkComment)
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404


class LMS_Content(APIView):
    def get(self, request, course_id, page_id):
        if page_id == "all":
            pages = (LMS_Page.objects.filter(course_id=course_id)).order_by('position_id')
            page_serializers = (LMS_PageSerializer(pages, many=True)).data
            for page in page_serializers:
                page_id = page['id']
                try:
                    component_querysets = (LMS_Component.objects.filter(page_id=page_id)).order_by('position_id')
                    component_serializers = (LMS_ComponentSerializer(component_querysets, many=True)).data
                    page['components'] = component_serializers
                except:
                    page['components'] = []
        else:
            page_queryset = get_object_or_404(LMS_Page, pk=page_id, course_id=course_id)
            page_serializers = (LMS_PageSerializer(page_queryset)).data
            try:
                component_querysets = (LMS_Component.objects.filter(page_id=page_id)).order_by('position_id')
                component_serializers = (LMS_ComponentSerializer(component_querysets, many=True)).data
                page_serializers['components'] = component_serializers
            except:
                page_serializers['components'] = []

        return JsonResponse(page_serializers, safe= False)
