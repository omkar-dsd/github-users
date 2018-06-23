from users_api.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    '''Generic serializer for Users API'''

    class Meta:
        model = User
        fields = '__all__'
