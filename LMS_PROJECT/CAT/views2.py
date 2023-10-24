from django.shortcuts import render
from .serializer import CAT_Course_Serializer, CAT_Course_Team_Serializer, CAT_Course_Lesson_Serializer,CAT_Course_Grading_Serializer, CAT_Course_Section_Serializer, CAT_Course_Question_Serializer, CAT_Course_Component_Serializer,CAT_Course_Subsection_Serializer, CAT_Courses_Resources_Serializer, CAT_Instructor_Serializer, CAT_Course_Group, CAT_Course_Group_Member
from .models import CAT_Course, CAT_Instructor, CAT_Course_Team, CAT_Course_Grading, CAT_Courses_Resources,CAT_Course_Section, CAT_Course_Subsection, CAT_Course_Lesson, CAT_Course_Component, CAT_Course_Question, CAT_Course_Group, CAT_Course_Group_Member
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse


class ContentViewSet(viewsets.ViewSet):
    def retrieve_content(request, id):
        course_queryset = CAT_Course.objects.all()
        course = get_object_or_404(course_queryset, pk=id)
        course_serializer = (CAT_Course_Serializer(course)).data
        question = CAT_Course_Question.objects.all()
        question_queryset = get_object_or_404(question, component_id__lesson_id__subsection_id__section_id__course_id=id)
        question_serializer = (CAT_Course_Question_Serializer(question_queryset)).data
        component = CAT_Course_Component.objects.all()
        component_queryset = get_object_or_404(component, lesson_id__subsection_id__section_id__course_id=id)
        component_serializer = (CAT_Course_Component_Serializer(component_queryset)).data
        lesson = CAT_Course_Lesson.objects.all()
        lesson_queryset = get_object_or_404(lesson, subsection_id__section_id__course_id=id)
        lesson_serializer = (CAT_Course_Lesson_Serializer(lesson_queryset)).data
        subsection = CAT_Course_Subsection.objects.all()
        subsection_queryset = get_object_or_404(subsection, section_id__course_id=id)
        subsection_serializer = (CAT_Course_Subsection_Serializer(subsection_queryset)).data
        section = CAT_Course_Section.objects.all()
        section_queryset = get_object_or_404(section, course_id=id)
        section_serializer = (CAT_Course_Section_Serializer(section_queryset)).data
        return JsonResponse([course_serializer, section_serializer, subsection_serializer, lesson_serializer, component_serializer, question_serializer], safe=False)



class CAT_InstructorViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Instructor.objects.all()
        serializer = CAT_Instructor_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Instructor.objects.all()
        instructor = get_object_or_404(queryset, pk=id)
        serializer = CAT_Instructor_Serializer(instructor)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Instructor_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Instructor.objects.all()
        instructor = get_object_or_404(queryset, pk=id)
        instructor.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Instructor.objects.all()
        instructor = get_object_or_404(queryset, pk=id)
        serializer = CAT_Instructor_Serializer(instructor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)



class CAT_Course_GroupViewSet(viewsets.ViewSet):
    def list_groups(request):
        queryset = CAT_Course_Group.objects.all()
        serializer = CAT_Course_Group_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve_group(request, id):
        group = CAT_Course_Group.objects.all()
        group_queryset = get_object_or_404(group, pk=id)
        group_serializer = (CAT_Course_Group_Serializer(group_queryset)).data
        group_member = CAT_Course_Group_Member.objects.all()
        group_member_queryset = get_object_or_404(group_member, group_id=id)
        group_member_serializer = (CAT_Course_Group_Member_Serializer(group_member_queryset)).data
        return JsonResponse([group_serializer, group_member_serializermember], safe=False)

    def create_group(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Group_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def create_group_member(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Group_Member_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete_group(request, id):
        queryset = CAT_Course_Group.objects.all()
        group = get_object_or_404(queryset, pk=id)
        group.delete()
        return HttpResponse(status=204)

    def delete_group_member(request, id):
        queryset = CAT_Course_Group_Member.objects.all()
        group_member = get_object_or_404(queryset, pk=id)
        group_member.delete()
        return HttpResponse(status=204)

        # to be decided later
    def update_goup(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Group.objects.all()
        group = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Group_Serializer(group, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)




class CAT_CourseViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Course.objects.all()
        serializer = CAT_Course_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course.objects.all()
        course = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Serializer(course)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Course.objects.all()
        course = get_object_or_404(queryset, pk=id)
        course.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course.objects.all()
        course = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Serializer(course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_Course_TeamViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Course_Team.objects.all()
        serializer = CAT_Course_Team_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course_Team.objects.all()
        course_team = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Team_Serializer(course_team)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Team_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Course_Team.objects.all()
        course_team = get_object_or_404(queryset, pk=id)
        course_team.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Team.objects.all()
        course_team = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Team_Serializer(course_team, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_Course_SectionViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Course_Section.objects.all()
        serializer = CAT_Course_Section_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course_Section.objects.all()
        course_section = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Section_Serializer(course_section)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Section_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Course_Section.objects.all()
        course_section = get_object_or_404(queryset, pk=id)
        course_section.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Section.objects.all()
        course_section = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Section_Serializer(course_section, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_Course_SubsectionViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Course_Subsection.objects.all()
        serializer = CAT_Course_Subsection_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course_Subsection.objects.all()
        course_subsection = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Subsection_Serializer(course_subsection)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Subsection_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Course_Subsection.objects.all()
        course_subsection = get_object_or_404(queryset, pk=id)
        course_subsection.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Subsection.objects.all()
        course_subsection = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Subsection_Serializer(course_subsection, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_Course_QuestionViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Course_Question.objects.all()
        serializer = CAT_Course_Question_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course_Question.objects.all()
        course_question = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Question_Serializer(course_question)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Question_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Course_Question.objects.all()
        course_question = get_object_or_404(queryset, pk=id)
        course_question.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Question.objects.all()
        course_question = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Question_Serializer(course_question, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_Course_ComponentViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Course_Component.objects.all()
        serializer = CAT_Course_Component_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course_Component.objects.all()
        course_component = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Component_Serializer(course_component)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Component_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Course_Component.objects.all()
        course_component = get_object_or_404(queryset, pk=id)
        course_component.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Component.objects.all()
        course_component = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Component_Serializer(course_component, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_Course_LessonViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Course_Lesson.objects.all()
        serializer = CAT_Course_Lesson_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course_Lesson.objects.all()
        course_lesson = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Lesson_Serializer(course_lesson)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Lesson_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Course_Lesson.objects.all()
        course_lesson = get_object_or_404(queryset, pk=id)
        course_lesson.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Lesson.objects.all()
        course_lesson = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Lesson_Serializer(course_lesson, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_Course_GradingViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Course_Grading.objects.all()
        serializer = CAT_Course_Grading_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course_Grading.objects.all()
        course_grading = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Grading_Serializer(course_grading)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Course_Grading_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Course_Grading.objects.all()
        course_grading = get_object_or_404(queryset, pk=id)
        course_grading.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course_Grading.objects.all()
        course_grading = get_object_or_404(queryset, pk=id)
        serializer = CAT_Course_Grading_Serializer(course_grading, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CAT_Course_ResourcesViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CAT_Courses_Resources.objects.all()
        serializer = CAT_Courses_Resources_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Courses_Resources.objects.all()
        course_resources = get_object_or_404(queryset, pk=id)
        serializer = CAT_Courses_Resources_Serializer(course_resources)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CAT_Courses_Resources_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CAT_Courses_Resources.objects.all()
        course_resources = get_object_or_404(queryset, pk=id)
        course_resources.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Courses_Resources.objects.all()
        course_resources = get_object_or_404(queryset, pk=id)
        serializer = CAT_Courses_Resources_Serializer(course_resources, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

def get_all_user_courses(request,user_id):
    course_list = []
    member = CAT_Course_Group_Member.objects.all()
    member_queryset = get_list_or_404(member, member_id=user_id)
    member_serializer = (CAT_Course_Group_Member_Serializer(member_queryset, many=True)).data
    for item in member_serializer:
        group_id = item['group_id']
        group = CAT_Course_Group.objects.all()
        group_queryset = get_object_or_404(group, pk=group_id)
        group_serializer = (CAT_Course_Group_Serializer(group_queryset)).data
        course_id = group_serializer['course_id']
        course = CAT_Course.objects.all()
        course_queryset = get_object_or_404(course, pk=course_id)
        course_serializer = (CAT_Course_Serializer(course_queryset)).data
        course_list.append(course_serializer)
    return JsonResponse(course_list, safe=False)
