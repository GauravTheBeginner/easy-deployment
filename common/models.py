import uuid
from common.manager import UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True, primary_key=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    profile_pic = models.ImageField(
        upload_to="media/profile_pics/",
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"
        ordering = ("last_login", "-is_active",)

    def __str__(self):
        return self.email


