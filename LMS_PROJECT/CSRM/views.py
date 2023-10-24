from django.shortcuts import render
from .serializer import Lookup_State_Serializer, Lookup_Country_Serializer, Lookup_Industry_Serializer,
CSRM_Institution_Serializer, CSRM_Institution_Office_Serializer, CSRM_Institution_Section_Serializer,
CSRM_Institution_Subsection_Serializer, CSRM_Institution_Member_Serializer, CSRM_User_Serializer, CSRM_User_Address_Serializer
from .models import Lookup_State, Lookup_Country, Lookup_Industry, CSRM_Institution, CSRM_Institution_Office,
CSRM_Institution_Section, CSRM_Institution_Subsection, CSRM_Institution_Member, CSRM_User, CSRM_User_Address
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

class CSRM_UserViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CSRM_User.objects.all()
        serializer = CSRM_User_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CSRM_User.objects.all()
        user = get_object_or_404(queryset, pk=id)
        serializer = CSRM_User_Serializer(user)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CSRM_User_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CSRM_User.objects.all()
        user = get_object_or_404(queryset, pk=id)
        user.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CSRM_User.objects.all()
        user = get_object_or_404(queryset, pk=id)
        serializer = CSRM_User_Serializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)



class CSRM_User_AddressViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CSRM_User_Address.objects.all()
        serializer = CSRM_User_Address_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course.objects.all()
        address = get_object_or_404(queryset, pk=id)
        serializer = CSRM_User_Address_Serializer(address)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CSRM_User_Address_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CSRM_User_Address.objects.all()
        address = get_object_or_404(queryset, pk=id)
        address.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CAT_Course.objects.all()
        address = get_object_or_404(queryset, pk=id)
        serializer = CSRM_User_Address_Serializer(address, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CSRM_InstitutionViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CSRM_Institution.objects.all()
        serializer = CSRM_Institution_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CAT_Course_Team.objects.all()
        institution = get_object_or_404(queryset, pk=id)
        serializer = CSRM_Institution_Serializer(institution)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CSRM_Institution_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CSRM_Institution.objects.all()
        institution = get_object_or_404(queryset, pk=id)
        institution.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CSRM_Institution.objects.all()
        institution = get_object_or_404(queryset, pk=id)
        serializer = CSRM_Institution_Serializer(institution, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CSRM_Institution_MemberViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CSRM_Institution_Member.objects.all()
        serializer = CSRM_Institution_Member_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CSRM_Institution_Member.objects.all()
        member = get_object_or_404(queryset, pk=id)
        serializer = CSRM_Institution_Member_Serializer(member)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CSRM_Institution_Member_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CSRM_Institution_Member.objects.all()
        member = get_object_or_404(queryset, pk=id)
        member.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CSRM_Institution_Member.objects.all()
        member = get_object_or_404(queryset, pk=id)
        serializer = CSRM_Institution_Member_Serializer(member, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CSRM_Institution_OfficeViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CSRM_Institution_Office.objects.all()
        serializer = CSRM_Institution_Office_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CSRM_Institution_Office.objects.all()
        office = get_object_or_404(queryset, pk=id)
        serializer = CSRM_Institution_Office_Serializer(office)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CSRM_Institution_Office_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CSRM_Institution_Office.objects.all()
        office = get_object_or_404(queryset, pk=id)
        office.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CSRM_Institution_Office.objects.all()
        office = get_object_or_404(queryset, pk=id)
        serializer = CSRM_Institution_Office_Serializer(office, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CSRM_Institution_SectionViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CSRM_Institution_Section.objects.all()
        serializer = CSRM_Institution_Section_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CSRM_Institution_Section.objects.all()
        section = get_object_or_404(queryset, pk=id)
        serializer = CSRM_Institution_Section_Serializer(section)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CSRM_Institution_Section_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CSRM_Institution_Section.objects.all()
        section = get_object_or_404(queryset, pk=id)
        section.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CSRM_Institution_Section.objects.all()
        section = get_object_or_404(queryset, pk=id)
        serializer = CSRM_Institution_Section_Serializer(section, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class CSRM_Institution_SubsectionViewSet(viewsets.ViewSet):
    def list(request):
        queryset = CSRM_Institution_Subsection.objects.all()
        serializer = CSRM_Institution_Subsection_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = CSRM_User_Subsection.objects.all()
        subsection = get_object_or_404(queryset, pk=id)
        serializer = CSRM_User_Subsection_Serializer(subsection)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = CSRM_User_Subsection_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = CSRM_User_Subsection.objects.all()
        subsection = get_object_or_404(queryset, pk=id)
        subsection.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = CSRM_User_Subsection.objects.all()
        subsection = get_object_or_404(queryset, pk=id)
        serializer = CSRM_User_Subsection_Serializer(subsection, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class Lookup_StateViewSet(viewsets.ViewSet):
    def list(request):
        queryset = Lookup_State.objects.all()
        serializer = Lookup_State_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = Lookup_State.objects.all()
        state = get_object_or_404(queryset, pk=id)
        serializer = Lookup_State_Serializer(state)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = Lookup_State_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = Lookup_State.objects.all()
        state = get_object_or_404(queryset, pk=id)
        state.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = Lookup_State.objects.all()
        state = get_object_or_404(queryset, pk=id)
        serializer = Lookup_State_Serializer(state, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class Lookup_CountryViewSet(viewsets.ViewSet):
    def list(request):
        queryset = Lookup_Country.objects.all()
        serializer = Lookup_Country_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = Lookup_Country.objects.all()
        country = get_object_or_404(queryset, pk=id)
        serializer = Lookup_Country_Serializer(country)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = Lookup_Country_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = Lookup_Country.objects.all()
        country = get_object_or_404(queryset, pk=id)
        country.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = Lookup_Country.objects.all()
        country = get_object_or_404(queryset, pk=id)
        serializer = Lookup_Country_Serializer(country, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class Lookup_IndustryViewSet(viewsets.ViewSet):
    def list(request):
        queryset = Lookup_Industry.objects.all()
        serializer = Lookup_Industry_Serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(request, id):
        queryset = Lookup_Industry.objects.all()
        industry = get_object_or_404(queryset, pk=id)
        serializer = Lookup_Industry_Serializer(industry)
        return JsonResponse(serializer.data)

    def create(request):
        data = JSONParser().parse(request)
        serializer = Lookup_Industry_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(request, id):
        queryset = Lookup_Industry.objects.all()
        industry = get_object_or_404(queryset, pk=id)
        industry.delete()
        return HttpResponse(status=204)

    def update(request, id):
        data = JSONParser().parse(request)
        queryset = Lookup_Industry.objects.all()
        industry = get_object_or_404(queryset, pk=id)
        serializer = Lookup_Industry_Serializer(industry, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
