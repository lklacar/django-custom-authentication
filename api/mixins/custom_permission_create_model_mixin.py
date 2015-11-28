from django.http import JsonResponse
from rest_framework import mixins

from api.mixins.custom_permission_mixin import CustomPermissionMixin


class CustomPermissionCreateModelMixin(CustomPermissionMixin, mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        if not self._is_allowed("create", request, self):
            return JsonResponse({"error": self.unauthorised_message})
        else:
            return super(CustomPermissionCreateModelMixin, self).create(request, *args, **kwargs)
