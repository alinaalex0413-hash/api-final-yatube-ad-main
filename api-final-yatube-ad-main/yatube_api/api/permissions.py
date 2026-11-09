# yatube_api/api/permissions.py
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение: чтение доступно всем,
    а изменение и удаление — только автору объекта.
    """

    def has_object_permission(self, request, view, obj):
        # Если запрос безопасный (GET, HEAD, OPTIONS) - разрешаем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Иначе проверяем, является ли пользователь автором
        return obj.author == request.user
