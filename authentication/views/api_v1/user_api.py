from rest_framework.permissions import IsAdminUser

from api.viewsets.custom_permission_model_view_set import CustomPermissionModelViewSet
from authentication.models import User
from authentication.serializers.user_serializer import UserSerializer


class AuthenticatedUserViewSet(CustomPermissionModelViewSet):
    """
    Only admin users can list other users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = {"list": IsAdminUser}
