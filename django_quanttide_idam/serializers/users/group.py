from rest_framework import serializers

from users.models.group import UserGroup


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"
