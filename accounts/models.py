from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserAccountManager(BaseUserManager):
    def create_admin(self, email, name, password=None, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Admin must be assigned to is_staff=True.")

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password=None, **other_fields):
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **other_fields)

        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=512, unique=True)
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserAccountManager()

    def get_full_name(self):
        return self.name

    def __str__(self):
        return f"<User name={self.get_full_name()} email={self.email}>"
