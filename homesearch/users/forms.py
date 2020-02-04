from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserInfo, Profile


class UserInfoCreationForm(UserCreationForm):
    is_agent = forms.BooleanField(required=False, initial=False, label='I am an Agent')

    class Meta(UserCreationForm):
        model = UserInfo
        fields = ('username', 'first_name', 'last_name', 'email')


class UserInfoChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = UserInfo
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    user_zip = forms.CharField(label='Zip Code', required=False)

    class Meta:
        model = Profile
        fields = ('user_zip', 'bio')


