from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser,Quiz,Question,Option,UserAnswer

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {    
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserAnswer)


