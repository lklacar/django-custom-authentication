from django.http import JsonResponse
from rest_framework import mixins

from api.mixins.custom_permission_mixin import CustomPermissionMixin


class CustomPermissionListModelMixin(CustomPermissionMixin, mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        if not self._is_allowed("list", request, self):
            return JsonResponse({"error": self.unauthorised_message})
        else:
            return super(CustomPermissionListModelMixin, self).list(request, *args, **kwargs)