"""
Ref:
  - https://django-organizations.readthedocs.io/en/latest/usage.html#views-mixins
"""

from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins

from organizations.models import Organization, OrganizationMember
from organizations.serializers import OrganizationSerializer, OrganizationMemberSerializer, OrganizationOwnerSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationMemberViewSet(ModelViewSet):
    serializer_class = OrganizationMemberSerializer

    def get_queryset(self):
        return OrganizationMember.objects.filter(organization=Organization.objects.get(name=self.kwargs['organization_name']))


class OrganizationOwnerView(
    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    serializer_class = OrganizationOwnerSerializer

    def update(self, request, *args, **kwargs):
        """
        TODO：重新定义为reset逻辑。

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass
