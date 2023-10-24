from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from LMS import models


# Import and Export Admin


@admin.register(models.LMS_Course)
@admin.register(models.LMS_Page)
@admin.register(models.LMS_Component)
@admin.register(models.LMS_Question)
@admin.register(models.LMS_Enrollment)
@admin.register(models.LMS_BookmarkComment)

class LMS_CourseAdmin(ImportExportModelAdmin):
    pass


# Customize Admin Portal Name
admin.site.site_header = "TQFE Administration"
admin.site.site_title = "TQFE Admin Portal"
admin.site.index_title = "Welcome to TQFE Server Administration Portal"
