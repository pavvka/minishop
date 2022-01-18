from django.contrib import admin
from django.contrib.auth.models import User

from user.models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)