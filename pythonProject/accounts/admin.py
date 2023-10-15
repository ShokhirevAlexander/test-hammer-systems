from django.contrib import admin
from .models import CustomeUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number',
                    'invite_code',
                    'password_phone',)


admin.site.register(CustomeUser, UserAdmin)
