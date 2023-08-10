from django_tenants.test.cases import TenantTestCase
from django.core.cache import cache

from users.models.user import User
from auth.forms.vcode import VCodeLoginForm


class VCodeLoginFormTestCase(TenantTestCase):
    form_class = VCodeLoginForm

    def setUp(self):
        # 登录
        self.vcode_login_data = {'phone_number': '18888888888', 'vcode': '123456'}
        User.objects.create(phone_number=self.vcode_login_data['phone_number'])
        cache.set('+86' + self.vcode_login_data['phone_number'], self.vcode_login_data['vcode'])
        # 注册
        self.vcode_signup_data = {'phone_number': '19999999999', 'vcode': '123456'}
        cache.set('+86' + self.vcode_signup_data['phone_number'], self.vcode_signup_data['vcode'])

    def test_is_valid_new(self):
        form = self.form_class(self.vcode_signup_data)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

    def test_is_valid_existed(self):
        # 模拟已存在
        form = self.form_class(self.vcode_login_data)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

    def test_save_new(self):
        form = self.form_class(self.vcode_signup_data)
        if form.is_valid():
            form.save()
        user = form.Meta.model.objects.get(phone_number=self.vcode_login_data['phone_number'])
        self.assertFalse(user.has_usable_password())

    def test_save_existed(self):
        form = self.form_class(self.vcode_login_data)
        if form.is_valid():
            form.save()
        user = form.Meta.model.objects.get(phone_number=self.vcode_login_data['phone_number'])
        self.assertTrue(user)
