from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

# from .models import MailCredential, UserProfile

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['id', 'email', 'mobile_no', 'rank', 'admin', 'otp']
    list_filter = ['admin', 'rank']
    fieldsets = (
        (None, {
            'fields': ('email', 'mobile_no', 'rank', 'password', 'has_profile')
        }),
        ('Personal info', {
            'fields': ('username',)
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'staff',
                'admin',
            )
        }),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'mobile_no', 'rank', 'password1', 'password2', 'has_profile')
            }
        ),
        ('Personal info', {
            'fields': ('username',)
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'staff',
                'admin',
            )
        }),
    )
    search_fields = [
        'email',
        'mobile_no',
        'rank',
    ]
    ordering = ['email']
    filter_horizontal = ()


# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'reporting_to', 'user')

#     class Meta:
#         model = UserProfile

# class MailCredentialAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email')

#     class Meta:
#         model = MailCredential

admin.site.register(User, UserAdmin)
# admin.site.register(UserProfile,UserProfileAdmin)
# admin.site.register(MailCredential,MailCredentialAdmin)
