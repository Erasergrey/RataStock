from rest_framework.permissions import BasePermission


class EsStaffParaEliminar(BasePermission):
    message = "Solo usuarios staff pueden eliminar productos."

    def has_permission(self, request, view):
        if request.method == "DELETE":
            return bool(request.user and request.user.is_staff)
        return True
