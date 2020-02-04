from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserInfoCreationForm, UserInfoChangeForm
from .models import UserInfo, Profile

# Register your models here.


class UserInfoAdmin(UserAdmin):
    add_form = UserInfoCreationForm
    form = UserInfoChangeForm
    model = UserInfo
    list_display = ['email', 'username', 'last_name', 'first_name', ]


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Profile)


