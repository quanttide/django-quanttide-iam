from django import forms

from users.models import User


class PasswordLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'password']

    def clean(self):
        cleaned_data = super().clean()
        # 验证手机
        phone_number = cleaned_data.get('phone_number')
        model_class = self.Meta.model
        try:
            self.instance = model_class.objects.get(phone_number=phone_number)
        except model_class.DoesNotExist:
            self.add_error('phone_number', "电话号码未注册")
        # 验证密码
        # Note: clean_password方法不可用，has_usable_password莫名其妙地结果错误。
        password = self.cleaned_data.get('password')
        if not self.instance.has_usable_password():
            self.add_error('password', '未设置密码')
        elif not self.instance.check_password(password):
            self.add_error('password', '密码错误')
        return cleaned_data
