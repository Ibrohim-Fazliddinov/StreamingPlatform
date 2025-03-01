from typing import Optional, Union
from django.contrib.auth.models import BaseUserManager

from users.utils import get_country_from_ip


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create(
        self,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        request=None,
        **extra_fields: Union[str, bool]
    ):
        if not (username or email or phone_number):
            raise ValueError("Must provide at least username, email, or phone_number")

        if email:
            email = self.normalize_email(email)

        if not username:
            username = email.split("@")[0]

        # Определяем страну по IP (если request передан)
        country_code = "CSM"
        if request:
            ip = request.META.get("REMOTE_ADDR")
            country_code = get_country_from_ip(ip)

        extra_fields["country"] = country_code

        user = self.model(username=username, **extra_fields)

        if email:
            user.email = email
        if phone_number:
            user.phone_number = phone_number
        if user.is_superuser:
            user.role = user.Role.ADMIN

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        request=None,
        **extra_fields: Union[str, bool]
    ):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)

        return self._create(phone_number, email, username, password, request, **extra_fields)

    def create_superuser(
        self,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        request=None,
        **extra_fields: Union[str, bool]
    ):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)

        return self._create(phone_number, email, username, password, request, **extra_fields)


