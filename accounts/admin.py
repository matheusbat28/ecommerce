from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', )
    search_fields = ('username', 'email', 'first_name', 'last_name', ) 
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('personal information', {
            'fields': ('first_name', 'last_name', 'telefone','perfil_img' )
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
admin.site.register(User, UserAdmin)