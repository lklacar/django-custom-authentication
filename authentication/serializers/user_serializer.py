from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'is_staff', "first_name", "last_name", "is_active", "date_joined", "last_login")
