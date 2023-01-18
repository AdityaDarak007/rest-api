from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create New User profile"""
        if not email:
            raise ValueError('USer must have an email address')

        """Make normalize the email except letter all letter small"""
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        """Encrypt the date"""
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email ,name , password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    """staff for admin"""
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['name']

    def get_full_name(self):
        """Retrive fullname of the users"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Retrieve string representation of our user"""
        return self.email


# Create your models here.
