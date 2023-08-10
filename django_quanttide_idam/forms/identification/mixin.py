from django.core.exceptions import ValidationError
from django.core.cache import cache


class VCodeValidationMixin:
    def validate_vcode(self, vcode):
        """
        验证码验证，从预设的缓存表中读取验证码并验证是否一致

        :param vcode: 用户输入验证码
        :return: vcode验证码原样返回，或者抛出验证错误

        TODO：增加对邮件验证码的支持，详见：https://quanttide.coding.net/p/qtapp/requirements/issues/279/detail。需要注意：
          - 增加邮件以后，函数命名和变量命名都需要修改；
          - 用户手机号或者邮件字段有无必要验证还需考虑，如果在Serializer类中完成则无需。
        """
        # TODO：添加"+86"只是一个临时补丁
        vcode2 = cache.get(self.cleaned_data['phone_number'].as_e164)
        if vcode != vcode2:
            raise ValidationError("验证码错误")
        return vcode
