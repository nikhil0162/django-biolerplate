from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, email, mobile_no, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not mobile_no:
            raise ValueError('Users must have a mobile_no number')

        user = self.model(mobile_no=mobile_no, email=self.normalize_email(email), **extra_fields)

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_staffuser(self, email, mobile_no, password=None, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(email, mobile_no, password=password, **extra_fields)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile_no, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, mobile_no, password=password, **extra_fields)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('full name'), max_length=250)
    rank = models.CharField(max_length=50, default='SHO')
    email = models.EmailField(max_length=250, unique=True)
    mobile_no = models.CharField(max_length=20, validators=[phone_validator], unique=True)
    otp = models.CharField(max_length=10, blank=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    has_profile = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_no']  # Email & Password are required by default.

    class Meta:
        ordering = ('-id',)

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin

    def __str__(self):
        return self.email

    def tokens(user):
        token = RefreshToken.for_user(user)
        return {'refresh': str(token), 'access': str(token.access_token)}
