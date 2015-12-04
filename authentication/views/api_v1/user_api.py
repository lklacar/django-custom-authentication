from rest_framework.permissions import IsAdminUser
from authentication.models import User
from authentication.serializers.user_serializer import UserSerializer
from custom_api_permissions.viewsets.custom_permission_model_view_set import CustomPermissionModelViewSet


class AuthenticatedUserViewSet(CustomPermissionModelViewSet):
    """
    Only admin users can list other users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = {"list": IsAdminUser, "retrieve": IsAdminUser, "update": IsAdminUser}
