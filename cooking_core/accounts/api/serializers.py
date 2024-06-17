from rest_framework.serializers import CharField, ModelSerializer

from cooking_core.accounts.models import User


class UserSerializerV1(ModelSerializer):
    password = CharField(min_length=2, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
