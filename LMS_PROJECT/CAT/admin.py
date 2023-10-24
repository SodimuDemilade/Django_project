from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import CAT_Course, CAT_Course_Team, CAT_Course_Lesson, CAT_Course_Grading, CAT_Course_Section,CAT_Course_Question, CAT_Course_Component, CAT_Course_Subsection, CAT_Courses_Resources, CAT_Instructor, CAT_Course_Group, CAT_Course_Group_Member


class CAT_Course_Group_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Course_Group_Member_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Instructor_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Course_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Course_Team_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Course_Lesson_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Course_Grading_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Course_Section_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Course_Question_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Course_Component_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Course_Subsection_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CAT_Courses_Resources_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(CAT_Course_Group, CAT_Course_Group_Admin)
admin.site.register(CAT_Course_Group_Member, CAT_Course_Group_Member_Admin)
admin.site.register(CAT_Instructor, CAT_Instructor_Admin)
admin.site.register(CAT_Course, CAT_Course_Admin)
admin.site.register(CAT_Course_Team, CAT_Course_Team_Admin)
admin.site.register(CAT_Course_Lesson, CAT_Course_Lesson_Admin)
admin.site.register(CAT_Course_Grading, CAT_Course_Grading_Admin)
admin.site.register(CAT_Course_Section, CAT_Course_Section_Admin)
admin.site.register(CAT_Course_Question, CAT_Course_Question_Admin)
admin.site.register(CAT_Course_Component, CAT_Course_Component_Admin)
admin.site.register(CAT_Course_Subsection, CAT_Course_Subsection_Admin)
admin.site.register(CAT_Courses_Resources, CAT_Courses_Resources_Admin)
