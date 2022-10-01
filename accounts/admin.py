from .models import Account
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class AccountAdmin(BaseUserAdmin):
    model = Account
    list_display = ('username', 'email', 'phone_number', 'dob', 'is_staff', 'is_admin', 'is_active') 

    filter_horizontal =()
    list_filter = ()
    fieldsets =()

admin.site.register(Account, AccountAdmin)    