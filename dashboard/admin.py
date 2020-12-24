from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Lic


@admin.register(Lic)
class LicAdmin(ImportExportModelAdmin):
	list_display =('name','email','dob','contact','address',
             'policy_type','policy_number','premium','sum_assured','year_of_policy'
             ,'beneficiary_name','created_on','renew_date','status')
    