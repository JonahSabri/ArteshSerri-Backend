from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'firstname', 'lastname', 'phone', 'jalali_created_at')
    fieldsets = (
        (None, {'fields': ('phone', 'password', 'decrypted_password')}),
        ('اطلاعات شخصی', {'fields': ('firstname', 'lastname', 'email')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('firstname', 'lastname', 'phone', 'password', 'decrypted_password'),
        }),
    )
    search_fields = ('firstname', 'lastname', 'phone')
    ordering = ('-created_at',)
    filter_horizontal = ()


admin.site.site_header = 'ارتش سری'
admin.site.index_title = 'ارتش سری'
admin.site.site_title = 'مدیریت'


admin.site.unregister(Group)
