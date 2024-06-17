from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from cooking_core.helpers.serializers import UserSerializerV1Hp

User = get_user_model()


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerV1Hp
