
class CustomPermissionMixin(object):
    permissions = {}
    unauthorised_message = "Unauthorised"
    method_keyword = ""

    def _is_allowed(self, method, request, c):
        print method not in self.permissions.keys()
        if method not in self.permissions.keys():
            return False

        permission = self.permissions[method]()
        return permission.has_permission(request, c)