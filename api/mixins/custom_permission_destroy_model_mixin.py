from django.http import JsonResponse
from rest_framework import mixins

from api.mixins.custom_permission_mixin import CustomPermissionMixin


class CustomPermissionDestroyModelMixin(CustomPermissionMixin, mixins.DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        if not self._is_allowed("destroy", request, self):
            return JsonResponse({"error": self.unauthorised_message})
        else:
            return super(CustomPermissionDestroyModelMixin, self).destroy(request, *args, **kwargs)
