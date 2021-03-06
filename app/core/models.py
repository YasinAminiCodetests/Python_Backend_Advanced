from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
                                        BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_feild):
        """create and saves a new user"""
        if not email:
            raise(ValueError)
        user = self.model(email=self.normalize_email(email), **extra_feild)
        user.set_password(password)
        user.save(using=self._db)
        # user
        return user

    def create_superuser(self, email, password):
        """creating the supper user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
