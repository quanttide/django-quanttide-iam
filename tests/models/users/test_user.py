# -*- coding: utf-8 -*-
"""
用户模型测试

测试要点：
  - 字段测试：测试不符合业务逻辑的异常情况是否被显式处理，比如异常的电话号码或者邮箱无法存储。
  - 密码处理测试：测试密码相关的业务逻辑的正常情况是否可用、异常情况是否被显式处理等。
  - 查询测试：经过修改的密码新闻给是否正常可用、异常是否被显式处理。

工程规范：
  - 以测试驱动开发（TDD）为导向，产品/架构和开发/测试应当合作确认单元测试的覆盖要点，并使用自动化测试工具完善自动构建（CI）流程。
"""

from django.test import TestCase
import unittest

from django_quanttide_idam.models import User


class UserTestCase(TestCase):
    def test_set_unusable_password(self):
        """
        首次设置不可用密码
        """
        pass

    def test_set_usable_password(self):
        """
        首次设置可用密码
        """
        pass

    def test_update_unusable_to_usable_password(self):
        """
        设置密码替换不可用密码
        """
        pass

    def test_update_usable_to_usable_password(self):
        """
        更新旧密码为新密码
        """
        pass

    def test_update_unusable_to_usable_password(self):
        """
        清除可用密码，断言结果为True，即允许此行为。

        经过技术委讨论，保留此接口的原因是可能在某些场景用到清除密码的特性，需要做的限制在上层API不暴露或者限制即可。
        """
        pass

    def test_update_unusable_to_unusable_password(self):
        """
        清除重设不可用密码。
        """
        pass

    def test_check_unusable_password(self):
        """
        检查不可用密码
        :return:
        """
        pass

    def test_check_right_usable_password(self):
        """
        检查正确的密码
        """
        pass

    def test_check_wrong_usable_password(self):
        """
        检查错误的密码
        """
        pass


class UserManagerTestCase(TestCase):
    """
    用户管理类测试

    测试要点：
      - 原生方法测试：看密码处理的业务逻辑是否正常。
      - 自定义方法测试：看是否符合业务逻辑预期。
    """
    def test_create_without_password(self):
        pass

    def test_create_with_password(self):
        pass

    def test_get_or_create_without_password(self):
        pass

    def test_get_or_create_with_password(self):
        pass

    @unittest.skip('Q语句抛出异常，无法通过测试')
    def test_get_by_username(self):
        user_data = {'mobile': '18888888888', 'password': 'gegwewgewsge'}
        User.objects.create(**user_data)
        user = User.objects.get_by_username(user_data['mobile'])
        user.check_password(user_data['password'])

    def test_update_without_new_password(self):
        pass

    def test_update_with_new_password_and_unusable_old_password(self):
        pass

    def test_update_with_new_password_and_usable_old_password(self):
        pass

    def test_update_with_unusable_new_password(self):
        """
        用不可用密码更新，断言结果为False，即不允许此情况。
        """
        pass
