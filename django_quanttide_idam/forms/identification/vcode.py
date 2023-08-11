from django import forms
from phonenumber_field.formfields import PhoneNumberField

from users.models import User
from .mixin import VCodeValidationMixin


class VCodeLoginForm(forms.ModelForm, VCodeValidationMixin):
    # bugfix: redefine to remove unique validator
    phone_number = PhoneNumberField()
    vcode = forms.CharField(max_length=6)

    class Meta:
        model = User
        fields = ['phone_number', 'verification_code']
        exclude = ['phone_number']  # bugfix: remove the model field to redefine

    def clean(self):
        cleaned_data = super().clean()
        # 验证验证码
        self.validate_vcode(cleaned_data['verification_code'])
        return cleaned_data

    def save(self, commit=True):
        instance, created = self.Meta.model.objects.get_or_create(phone_number=self.cleaned_data['phone_number'])
        return instance

