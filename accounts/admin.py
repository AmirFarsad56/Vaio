from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import UserModel
from accounts.forms import UserForm
from commonuser.models import CommonUserModel


class CommonUserInline(admin.StackedInline):
    model = CommonUserModel
    can_delete = False
    verbose_name_plural = 'CommonUser'
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = UserForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username','email','date_joined')
    list_filter = ('is_commonuser','is_sportclub','is_superuser')
    fieldsets = (
        ('Personal Info', {'fields': ('username','email', 'password','is_commonuser','is_sportclub')}),
        ('Date Info', {'fields': ('last_login','date_joined')}),
        ('Permissions', {'fields': ('is_active','is_superuser','is_staff')}),
    )


    search_fields = ('username','email',)
    ordering = ('-date_joined',)
    #Registering the CommonUserModel
    inlines = [CommonUserInline,]


#registering the model
admin.site.register(UserModel,UserAdmin)


