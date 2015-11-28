from django.http import JsonResponse
from rest_framework import mixins

from api.mixins.custom_permission_mixin import CustomPermissionMixin


class CustomPermissionUpdateModelMixin(CustomPermissionMixin, mixins.UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        if not self._is_allowed("update", request, self):
            return JsonResponse({"error": self.unauthorised_message})
        else:
            return super(CustomPermissionUpdateModelMixin, self).update(request, *args, **kwargs)
