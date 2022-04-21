from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# ==================================Custom user model======================================
class MyAccountManager(BaseUserManager):
    """
    Custom manager for creating users and superusers
    """

    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('User must have an email')

        user = self.model(
            email=self.normalize_email(email),
            username=email.split('@')[0],
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    """
    Custom user model. To override built-in user model add this to settings.py:

    AUTH_USER_MODEL = 'accounts.Account'  # your custom model
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    # required for custom user tables
    date_joined = models.DateTimeField(auto_now_add=True)
    date_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # enable logging in with an email
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()  # overrisde standard manager

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):  # required
        return self.is_admin

    def has_module_perms(self, add_label):  # required
        return True
# ==========================END of Custom user model====================================
