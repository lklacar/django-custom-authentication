from django.http import JsonResponse
from rest_framework import mixins

from api.mixins.custom_permission_mixin import CustomPermissionMixin


class CustomPermissionRetriveModelMixin(CustomPermissionMixin, mixins.RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        if not self._is_allowed("retrieve", request, self):
            return JsonResponse({"error": self.unauthorised_message})
        else:
            return super(CustomPermissionRetriveModelMixin, self).retrieve(request, *args, **kwargs)
