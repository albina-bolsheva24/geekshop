import hashlib

import pytz
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from authapp.models import ShopUser, ShopUserProfile
from datetime import datetime


class ShopUserLoginForms(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_texts = ''


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'avatar', 'email', 'age', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_texts = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Слишком молод!')
        return data

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.is_active = False
        user.activate_key = hashlib.sha1(user.email.encode('utf8')).hexdigest()
        user.activate_key_expired = datetime.now(pytz.timezone(settings.TIME_ZONE))
        user.save()

        return user


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'avatar', 'email', 'age', 'password')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_texts = ''
                if field_name == 'password':
                    field.widget = forms.HiddenInput()


def clean_age(self):
    data = self.cleaned_data['age']
    if data < 18:
        raise forms.ValidationError('Слишком молод!')
    return data


# def clean_email(self):
#   data = self.cleaned_data['email']
#   is_exists = ShopUser.objects.exclude(pk=self.instance.pk).filter(email=data).exists)
#   if

class ShopUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = ShopUserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_texts = ''

