from rest_framework import serializers

from organizations.models import Organization, OrganizationOwner, OrganizationMember


class OrganizationMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMember
        exclude = ('organization', )


class OrganizationOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationOwner
        exclude = ('organization', )


class OrganizationSerializer(serializers.ModelSerializer):
    owner = OrganizationOwnerSerializer()
    members = OrganizationMemberSerializer(many=True)

    class Meta:
        model = Organization
        fields = '__all__'
