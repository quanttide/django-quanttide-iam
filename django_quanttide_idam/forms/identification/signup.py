from django import forms

from users.models import User
from .mixin import VCodeValidationMixin


class PasswordSignUpForm(forms.ModelForm, VCodeValidationMixin):
    password2 = forms.CharField(max_length=128)
    vcode = forms.CharField(max_length=6)

    class Meta:
        model = User
        fields = ['phone_number', 'password', 'password2', 'vcode']

    def clean(self):
        cleaned_data = super().clean()
        # 验证验证码
        self.validate_vcode(cleaned_data['vcode'])
        # 验证密码设置
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            self.add_error('password', "两次输入的密码不一致")
        return cleaned_data

    def save(self, commit=True):
        instance = self.Meta.model.objects.create(phone_number=self.cleaned_data['phone_number'],
                                                  password=self.cleaned_data['password'])
        return instance
