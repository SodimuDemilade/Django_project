from rest_framework.views import APIView
from .models import (CEC_Course, CEC_NewCourse, CEC_TopCourse, CEC_FeaturedCourse)
from .serializer import CEC_CourseSerializer
from django.http import JsonResponse


class coursedetail(APIView):
    def get(self, request, new, top, featured, subcategory_id, learning_style, price_range, institution_id, search_text):
        queryset = CEC_Course.objects.all()
        if new == "Y":
            queryset = queryset.filter(cec_topcourse__is_removed="False")
        if top == "Y":
            queryset = queryset.filter(cec_newcourse__is_removed="False")
        if featured == "Y":
            queryset = queryset.filter(cec_featuredcourse__is_removed="False")
        if learning_style != "A":
            queryset = queryset.filter(learning_style=learning_style)
        if price != "A":
            queryset = queryset.filter(price=price)
        if institution_id != "A":
            queryset = queryset.filter(institution_id=institution_id)
        serializer = CEC_CourseSerializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)
