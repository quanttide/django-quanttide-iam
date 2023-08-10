"""
Ref:
  - https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_many/
  - https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
"""
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status

from users.models.user import User
from users.models.group import UserGroup
from users.serializers.group import UserGroupSerializer
from staff.permissions import IsStaff


class UserGroupViewSet(ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    lookup_field = 'name'
    permission_classes = [IsStaff]

    @action(detail=True, methods=['POST'], url_path='add-user')
    def add_user(self, request, name):
        """

        :return:
        """
        group = UserGroup.objects.get(name=name)
        user = User.objects.get(phone_number=request.data['phone_number'])
        group.users.add(user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'], url_path='remove-user')
    def remove_user(self, request, name):
        """

        :return:
        """
        group = UserGroup.objects.get(name=name)
        user = User.objects.get(phone_number=request.data['phone_number'])
        group.users.remove(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
