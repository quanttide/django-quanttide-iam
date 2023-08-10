"""
Identification and Authorization APIs
"""




# class AuthorizationView(AuthorizationServer, APIView):
#     """
#     `AuthorizationServer` implements for Django REST Framework
#
#     Note: 未来拆分到`drf-authlib-provider`(或者`drf-authlib`)开源库，用来在私有化场景复用实现。
#     """
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def query_client(self, client_id):
#         try:
#             return Client.objects.get(client_id=client_id)
#         except Client.DoesNotExist:
#             return None
#
#     def save_token(self, token, request):
#         raise NotImplementedError('没有必要存Token')
#
#     def send_signal(self, name, *args, **kwargs):
#         pass
#
#     def create_oauth2_request(self, request):
#         pass
#
#     def create_json_request(self, request):
#         pass
#
#     def handle_response(self, status, body, headers):
#         return Response(status=status, data=body, headers=headers)
#
#     def handle_error_response(self, request, error):
#         return super().handle_error_response(request, error)
#
#     def validate(self, *args, **kwargs):
#         raise NotImplementedError()
#
#     def post(self, request):
#         serializer = self.get_serializer(request.data)
#         if serializer.is_valid():
#             if serializer.instance is None:
#                 serializer.save()
#             return self.create_authorization_response(request, grant_user=request.user)
#         return self.create_authorization_response(request, grant_user=None)

