from django import forms


# class WechatLoginForm(identification.ModelForm):
#     """
#     微信登录或注册的序列化类
#     """
#     # id_token = users.CharField(max_length=64)
#
#     class Meta:
#         model = WechatUser
#         exclude = ['wechat_user_id', 'instance']
#
#     def to_interval_value(self, data):
#         """
#         加工反序列化数据的原始数据格式
#         :param data:
#         :return:
#         """
#         data.update({
#             'openid_'+data['client_label']: data['openid'],
#         })
#         return super().to_interval_value(data)
#
#     def create(self, validated_data):
#         # 生成新基本用户
#         user = User.objects.create()
#         # unionid字段
#         unionid = validated_data.get('unionid', None)
#         # openid字段
#         # TODO：优化实现，和to_interval_value方法一起重新审视。
#         kwargs = {}
#         if 'client_label' in validated_data:
#             openid_field = 'openid_' + validated_data['client_label']
#             openid = validated_data.get('openid', None)
#             kwargs[openid_field] = openid
#         # 创建实例
#         instance = self.Meta.model.objects.create(user=user, unionid=unionid, **kwargs)
#         return instance
