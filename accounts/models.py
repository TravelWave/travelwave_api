from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("phone number required.")

        user = self.mode(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)

    is_staff = models.BooleanField(default=True)
    is_driver = models.BooleanField(default=False)
    driver_license = models.ImageField(
        upload_to="driver_license/",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.phone_number

    def has_perm(self, perm: str, obj: None) -> bool:
        return self.is_staff

    def has_module_perms(self, app_label: str) -> bool:
        return self.is_staff
