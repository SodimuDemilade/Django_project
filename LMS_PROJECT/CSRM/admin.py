from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from .models import Lookup_State, Lookup_Country, Lookup_Industry, CSRM_Institution, CSRM_Institution_Office,CSRM_Institution_Section, CSRM_Institution_Subsection, CSRM_Institution_Member, CSRM_User, CSRM_User_Address

class CSRM_User_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CSRM_User_Address_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CSRM_Institution_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CSRM_Institution_Member_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CSRM_Institution_Office_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CSRM_Institution_Section_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CSRM_Institution_Subsection_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class Lookup_State_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class Lookup_Country_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class Lookup_Industry_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(CSRM_User, CSRM_User_Admin)
admin.site.register(CSRM_User_Address, CSRM_User_Address_Admin)
admin.site.register(CSRM_Institution, CSRM_Institution_Admin)
admin.site.register(CSRM_Institution_Member, CSRM_Institution_Member_Admin)
admin.site.register(CSRM_Institution_Office, CSRM_Institution_Office_Admin)
admin.site.register(CSRM_Institution_Section, CSRM_Institution_Section_Admin)
admin.site.register(CSRM_Institution_Subsection, CSRM_Institution_Subsection_Admin)
admin.site.register(Lookup_State, Lookup_State_Admin)
admin.site.register(Lookup_Country, Lookup_Country_Admin)
admin.site.register(Lookup_Industry, Lookup_Industry_Admin)
