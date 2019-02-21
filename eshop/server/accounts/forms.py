from django import forms
from .models import AccountUser
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserChangeForm
# from .models import AccountUser


# class AccountUserModelForm(AuthenticationForm):
#     class Meta:
#         model = AccountUser
#         fields = ('username', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super(AccountUserModelForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
#
# class AccountUserRegisterForm(UserCreationForm):
#     class Meta:
#         model = AccountUser
#         fields = ('username', 'first_name', 'password1', 'password2', 'email', 'phone', 'avatar')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#             field.help_text = ''
#
#
# class AccountUserEditForm(UserChangeForm):
#     class Meta:
#         model = AccountUser
#         fields = ('username', 'first_name', 'email', 'phone', 'avatar', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#             field.help_text = ''
#             if field_name == 'password':
#                 field.widget = forms.HiddenInput()

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=128)
    password = forms.CharField(required=True, max_length=72, widget=forms.widgets.PasswordInput())


class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(required=True, max_length=72, widget=forms.widgets.PasswordInput())

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password is not confirm')
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)
        if commit:
            user.save()
        return user

    class Meta:
        model = AccountUser
        fields = ['username', 'password']
        widgets = {
            'password': forms.widgets.PasswordInput()
        }

