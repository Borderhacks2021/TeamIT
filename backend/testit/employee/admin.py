from django.contrib import admin

from employee.models import Employee, EmployeeProgramSkills, EmployeeMBTI, EmployeeWorkingGenius, EmployeeColourTraits

admin.site.register(Employee)
admin.site.register(EmployeeProgramSkills)
admin.site.register(EmployeeMBTI)
admin.site.register(EmployeeWorkingGenius)
admin.site.register(EmployeeColourTraits)