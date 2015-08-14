import datetime

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, instance=None, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if instance:
            instance.set_password(password)
            instance.save()
            return instance
        email = self.normalize_email(email)
        extra_fields["last_login"] = datetime.datetime.now()
        user = self.model(email=email, **extra_fields)
        if not password:
            user.set_unusable_password()
        else:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        self.create_user(email, password, is_superuser=True, **extra_fields)
