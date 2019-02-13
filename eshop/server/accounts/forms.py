from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import AccountUser


class AccountUserModelForm(AuthenticationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(AccountUserModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AccountUserRegisterForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class AccountUserEditForm(UserChangeForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'first_name', 'email', 'phone', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

