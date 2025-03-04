from rest_framework.permissions import BasePermission, SAFE_METHODS


class ContentViewSetPermissions(BasePermission):

    """
      Разрешения для работы с контентом в `ContentViewSet`.

      Определяет, кто имеет доступ к методам API:
      - `GET`: доступ открыт для всех пользователей.
      - `POST`, `PUT`, `DELETE`: доступ только для аутентифицированных пользователей.
      - Методы изменения разрешены только владельцу контента или администратору.
      """

    def has_permission(self, request, view):
        """
               Проверяет, есть ли у пользователя разрешение для выполнения операции.
        """
        match request.method:
            case 'GET':
                return True
            case 'POST' | 'PUT' | 'DELETE':
                return request.user and request.user.is_authenticated
            case _:
                return False

    def has_object_permission(self, request, view, obj):
        """
                Проверяет, есть ли у пользователя разрешение на доступ к объекту.
        """
        if request.method in SAFE_METHODS:
            return True

        # Методы записи разрешены только владельцу или администратору
        return obj.author == request.user or request.user.is_staff