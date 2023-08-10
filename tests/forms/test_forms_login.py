from django_tenants.test.cases import TenantTestCase

from users.models.user import User
from auth.forms.login import PasswordLoginForm


class PasswordLoginFormTestCase(TenantTestCase):
    form_class = PasswordLoginForm

    def setUp(self):
        super().setUp()
        self.login_data = {'phone_number': '+8618888888888', 'password': 'gegwewgewsge'}
        self.login_data_mobile_error = {'phone_number': '+8617777777777', 'password': 'cest'}
        self.login_data_password_unset = {'phone_number': '+8619999999999', 'password': 'gegwewgewsge'}
        self.login_data_password_error = {'phone_number': '+8618888888888', 'password': 'gegwewgew'}
        self.user = User.objects.create(**self.login_data)
        self.assertTrue(self.user.has_usable_password())
        self.assertTrue(self.user.check_password(self.login_data['password']))
        self.user_without_password = User.objects.create(phone_number=self.login_data_password_unset['phone_number'])
        self.assertFalse(self.user_without_password.has_usable_password())

    def test_is_valid(self):
        form = self.form_class(self.login_data)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

    def test_is_valid_phone_number_error(self):
        form = self.form_class(self.login_data_mobile_error)
        is_valid = form.is_valid()
        self.assertFalse(is_valid)
        self.assertEqual('电话号码未注册', form.errors['phone_number'][0])

    def test_is_valid_password_unset(self):
        form = self.form_class(self.login_data_password_unset)
        is_valid = form.is_valid()
        self.assertFalse(is_valid)
        self.assertEqual('未设置密码', form.errors['password'][0])

    def test_is_valid_password_error(self):
        form = self.form_class(self.login_data_password_error)
        is_valid = form.is_valid()
        self.assertFalse(is_valid)
        self.assertEqual('密码错误', form.errors['password'][0])
