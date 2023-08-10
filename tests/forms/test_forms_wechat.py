from django_tenants.test.cases import TenantTestCase


class WechatLoginFormTestCase(TenantTestCase):
    # form_class = WechatLoginForm

    def test_is_valid_new(self):
        pass
        # data = {'id_token': 'test', 'openid': 'test', 'client_label': 'wxopen_quanttide'}
        # serializer = self.serializer_class(data=data)
        # self.assertTrue(serializer.is_valid())

    def test_is_valid_existed(self):
        pass

    def test_save_new(self):
        pass
        # data = {'id_token': 'test', 'openid': 'test', 'client_label': 'wxopen_quanttide'}
        # serializer = self.serializer_class(data=data)
        # if serializer.is_valid():
        #     wechatuser = serializer.save()
        #     self.assertTrue(isinstance(wechatuser, self.serializer_class.Meta.model))

    def test_save_existed(self):
        pass

