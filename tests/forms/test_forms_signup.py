from django_tenants.test.cases import TenantTestCase
from django.core.cache import cache

from auth.forms.signup import PasswordSignUpForm


class PasswordSignUpFormTestCase(TenantTestCase):
    form_class = PasswordSignUpForm

    def setUp(self):
        self.signup_data = {'phone_number': '19999999999', 'verification_code': '123456', 'password': 'ge34ttgxt43',
                            'password2': 'ge34ttgxt43'}  #
        # 设置缓存模拟验证码发送
        cache.set('+86' + self.signup_data['phone_number'], self.signup_data['verification_code'])

    def test_is_valid(self):
        form = self.form_class(self.signup_data)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

    def test_save(self):
        form = self.form_class(self.signup_data)
        if form.is_valid():
            form.save()
        user = form.Meta.model.objects.get(phone_number=self.signup_data['phone_number'])
        checked = user.check_password(self.signup_data['password'])
        self.assertTrue(checked)
