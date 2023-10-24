from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CEC_Course, CEC_NewCourse, CEC_TopCourse, CEC_FeaturedCourse


class CEC_Course_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CEC_NewCourse_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CEC_TopCourse_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CEC_FeaturedCourse_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(CEC_Course, CEC_Course_Admin)
admin.site.register(CEC_NewCourse, CEC_NewCourse_Admin)
admin.site.register(CEC_TopCourse, CEC_TopCourse_Admin)
admin.site.register(CEC_FeaturedCourse, CEC_FeaturedCourse_Admin)
