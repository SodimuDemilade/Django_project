from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializer import (CAT_Course_Serializer, CAT_Course_Team_Serializer, CAT_CourseLessonSerializer,
CAT_Course_Grading_Serializer, CAT_CourseSectionSerializer, CAT_Course_Question_Serializer, CAT_CourseComponentSerializer,
CAT_CourseSubsectionSerializer, CAT_Courses_Resources_Serializer, CAT_Instructor_Serializer, CAT_Course_Group_Serializer,
CAT_Course_Group_Member_Serializer, CAT_All_Course_list_Serializer, CAT_Course_Edit_Serializer, CAT_CourseEditSectionSerializer, CAT_CourseEditSubsectionSerializer,
CAT_CourseEditLessonSerializer, CAT_CourseEditComponentSerializer)
from .models import (CAT_Course, CAT_Instructor, CAT_Course_Team, CAT_Course_Grading, CAT_Courses_Resources,CAT_Course_Section,
CAT_Course_Subsection, CAT_Course_Lesson, CAT_Course_Component, CAT_Course_Question, CAT_Course_Group, CAT_Course_Group_Member)
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import RetrieveUpdateAPIView


class ListUsers(APIView):
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        PASS

class CAT_LogView(APIView):

    def get(self, request, format=None):
        PASS

class CAT_CourseListCreateView(APIView):

    def get(request, format=None):
        queryset = CAT_Course.objects.all()
        serializer = CAT_Course_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            course = get_object_or_404(CAT_Course, name=data["name"])
            course_serializer = (CAT_Course_Edit_Serializer(course)).data
            course_id = course_serializer["id"]
            team = {"course_id":course_id, "member_id":data["created_by_id"], "role":"L"}
            team_serializer = CAT_Course_Team_Serializer(data=team)
            if team_serializer.is_valid():
                team_serializer.save()
                return JsonResponse(team_serializer.data, safe=False)
            return JsonResponse(team_serializer.errors, status=400)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def put(request, id):
        data = JSONParser().parse(request)
        course = get_object_or_404(CAT_Course, pk=id)
        serializer = CAT_Course_Edit_Serializer(course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    # def get_course_with_instructor(request, course_id):
    #     course = CAT_Course.objects.all()
    #     course_queryset = get_object_or_404(course, pk=course_id)
    #     course_serializer = CAT_All_Course_list_Serializer(course_queryset).data
    #     return JsonResponse(course_serializer, safe=False)

    def get_all_courses_with_instructor(request):
        course = CAT_Course.objects.all()
        course_serializer = CAT_All_Course_list_Serializer(course, many=True).data
        return JsonResponse(course_serializer, safe=False)

class CAT_CourseSectionView(APIView):
    def post(request):
        data = JSONParser().parse(request)
        serializer = CAT_CourseSectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

        def put(request, id):
            data = JSONParser().parse(request)
            section = get_object_or_404(CAT_Course_Section, pk=id)
            serializer = CAT_CourseEditSectionSerializer(section, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors, status=400)


class CAT_CourseSubsectionView(APIView):
    def post(request):
        data = JSONParser().parse(request)
        serializer = CAT_CourseEditSubsectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

        def put(request, id):
            data = JSONParser().parse(request)
            subsection = get_object_or_404(CAT_Course_Subsection, pk=id)
            serializer = CAT_CourseSubsectionSerializer(subsection, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors, status=400)


class CAT_CourseLessonView(APIView):
    def post(request):
        data = JSONParser().parse(request)
        serializer = CAT_CourseLessonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

        def put(request, id):
            data = JSONParser().parse(request)
            lesson = get_object_or_404(CAT_Course_Lesson, pk=id)
            serializer = CAT_CourseEditLessonSerializer(subsection, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors, status=400)


class CAT_CourseComponentView(APIView):
    def post(request):
        data = JSONParser().parse(request)
        serializer = CAT_CourseComponentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

        def put(request, id):
            data = JSONParser().parse(request)
            commponent = get_object_or_404(CAT_Course_Component, pk=id)
            serializer = CAT_CourseEditLessonSerializer(component, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors, status=400)


class CAT_CourseDetailEditView(APIView):

    def get(request, id):
        course = get_object_or_404(CAT_Course, pk=id)
        serializer = CAT_Course_Edit_Serializer(course)
        return JsonResponse(serializer.data)


class CAT_GradingEditView(APIView):

    def post(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Grading_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    def put(request):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Grading.objects.all()
        course_grading = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Grading_Serializer(course_grading, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_TeamEditView(APIView):

    def post(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Team_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    def put(request):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Team.objects.all()
        course_team = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Team_Serializer(course_team, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_GroupEditView(APIView):
    def get(request, id):
        group = CAT_Course_Group.objects.all()
        group_queryset = get_object_or_404(group, pk=id)
        group_serializer = (CAT_Course_Group_Serializer(group_queryset)).data
        group_member = CAT_Course_Group_Member.objects.all()
        group_member_queryset = get_object_or_404(group_member, group_id=id)
        group_member_serializer = (CAT_Course_Group_Member_Serializer(group_member_queryset)).data
        return JsonResponse([group_serializer, group_member_serializermember], safe=False)

    def post(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Group_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def put(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Group.objects.all()
        group = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Group_Serializer(group, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    # def create_group_member(request):
    #     data = JSONParser().parse(request)
    #     serializer = CAT_Course_Group_Member_Serializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)


class CAT_ResourceEditView(APIView):
    def post(request):
        data = JSONParser().parse(request)
        serializer = CAT_Courses_Resources_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    def put(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Courses_Resources.objects.all()
        course_resources = get_object_or_404(queryset, pk=id)
        serializer = CAT_Courses_Resources_Serializer(course_resources, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

class CAT_ContentEditView(APIView):
    def retrieve_content(request, id):
        course_queryset = CAT_Course.objects.all()
        course = get_object_or_404(course_queryset, pk=id)
        course_serializer = (CAT_Course_Serializer(course)).data
        courses = course_serializer
        section = CAT_Course_Section.objects.all()
        section_queryset = get_list_or_404(section, course_id=id)
        section_serializer = (CAT_Course_Section_Serializer(section_queryset, many=True)).data
        sections = section_serializer
        for section in sections:
            courses['sections'] = sections
            section_id = section['id']
            subsection = CAT_Course_Subsection.objects.all()
            subsection_queryset = get_list_or_404(subsection, section_id=section_id)
            subsection_serializer = (CAT_Course_Subsection_Serializer(subsection_queryset, many=True)).data
            subsections = subsection_serializer
            section['subsections'] = subsections
            for subsection in subsections:
                subsection_id = subsection['id']
                lesson = CAT_Course_Lesson.objects.all()
                lesson_queryset = get_list_or_404(lesson, subsection_id=subsection_id)
                lesson_serializer = (CAT_Course_Lesson_Serializer(lesson_queryset, many=True)).data
                lessons = lesson_serializer
                subsection['lessons'] = lessons
                for lesson in lessons:
                    lesson_id = lesson['id']
                    component = CAT_Course_Component.objects.all()
                    component_queryset = get_list_or_404(component, lesson_id=lesson_id)
                    component_serializer = (CAT_Course_Component_Serializer(component_queryset, many=True)).data
                    components = component_serializer
                    lesson['components'] = components
        return JsonResponse([course_serializer], safe=False)

class LookupAndChoiceView(APIView):
    def choices(request):
        lookup = {}
        lookup['gender'] = [['M', 'MALE'], ['F', 'FEMALE'], ['NOT', 'NOT DECLARED']]
        lookup['age'] = [['<18', 'UNDER 18'], ['18-24', 'BETWEEN 18 AND 24'], ['25-34', 'BETWEEN 35 AND 44'], ['45-54', 'BETWEEN 45 AND 54'],
        ['55-64', 'BETWEEN 55 AND 64'], ['65-74', 'BETWEEN 65 AND 74'], ['>75', 'OLDER THAN 75']]
        lookup['emp'] = [['S', 'STUDENT'],['U', 'UNEMPLOYED'],['SE', 'SELF-EMPLOYED'],
        ['CE', 'COMAPNY-EMPLOYED'],['OM', 'OWNER-MANAGER']]
        lookup['marital'] = [['S', 'SINGLE'],['M', 'MARRIED'],['D/W', 'DIVORCED/WIDOWED'],['NOT', 'NOT DECLARED']]
        lookup['exp'] = [['B', 'BEGINNER'],['I', 'INTERMEDIATE'],['E', 'EXPERT']]
        lookup['edu'] = [['P', 'PRIMARY'],['S', 'SECONDARY'],['TT/D', 'TRADE TEST/DIPLOMA'],
        ['H/B', 'HND/BACHELORS'],['M', 'MASTERS'],['P', 'PHD']]
        lookup['language'] = [['E', 'ENGLISH'],['F', 'FRENCH'],['C', 'CHINESE'],['Y', 'YORUBA'],
        ['H', 'HAUSA'],['I', 'IGBO']]
        lookup['stat'] = [['A', 'ACTIVE'],['M', 'MERGED'],['D', 'DEACTIVATED']]
        lookup['level'] = [['I', 'INTRODUCTORY'],['IN', 'INTERMEDIATE'],['A', 'ADVANCED']]
        lookup['pacing'] = [['I', 'INSTRUCTOR-LED'],['S', 'SELF-PACED']]
        lookup['enrollment'] =[['O', 'OPEN'], ['B', 'BY_INVITATION']]
        lookup['publication'] = [['DN', 'DRAFT(NEVER PUBLISHED)'],['P', 'PUBLISHED(NOT YET RELEASED)'],['PL', 'PUBLISHED AND LIVE'],['DU', 'DRAFT(UNPUBLISHED CHANGES)']]
        lookup['user_type'] = [['LA', 'LEAD AUTHOR'],['AU', 'AUTHOR'],['L', 'LEARNER']]
        lookup['role'] = [['S', 'STAFF'],['L', 'LEAD',],['A', 'AUTHOR'],['R', 'READER']]
        lookup['resources_type'] = [['I', 'IMAGE'],['V', 'VIDEO'],['H', 'HTML'],['P', 'PDF'],
        ['W', 'WORD'],['E', 'EXCEL'],['PP', 'POWERPOINT'],['O', 'OTHERS']]
        lookup['component_type'] = [['V', 'VIDEO'],['I', 'IMAGE'],['H', 'HTML'],['E', 'EXERCISE']]
        lookup['video'] = [['V', 'VIMEO'],['Y', 'YOUTUBE'],['M', 'MP4'],['WZ', 'WEBINAR ON ZOOM'],
        ['ME', 'MEETING ON ZOOM'],['WV', 'WEBINAR ON VIMEO']]
        lookup['html'] = [['H', 'HTML'],['I', 'IFRAME']]
        lookup['exercise_type'] = [['V', 'QUIZ'],['Y', 'ONLINETEST'],['M', 'OFFLINETEST']]
        lookup['question_type'] = [['T', 'TEXT'],['N', 'NUMBER'],['R', 'RADIOBUTTON'],
        ['C', 'CHECKBOX'],['DR', 'DROPDOWN'],['E', 'ESSAY'],['D', 'DISCUSSION']]
        return JsonResponse(lookup, safe=False)


# ///////////////////////////////////////////////
# SEPARATE VIEW FOR TESTING SIGNALS AND THREADS
# //////////////////////////////////////////////
def enroll_student(request):
    # Send email asynchronously
    subject = "Course Enrollment Confirmation"
    message = "Thank you for enrolling in our course."
    from_email = "your@email.com"
    recipient_list = [user_email]
    send_email_async(subject, message, from_email, recipient_list)

    # Return the response
    return Response({'message': 'Enrollment successful'})
