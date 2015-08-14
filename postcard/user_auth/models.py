from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

# Create your models here.
class User(AbstractBaseUser):

    full_name = models.CharField(max_length=130, default="")
    email = models.EmailField(unique=True, db_index=True, blank=False)

    #: An attribute that tells Django which field should be treated as the username field. In our case, it is the :attr:`email` field.
    USERNAME_FIELD = "email"
    
    joined_on = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=True, default=None)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # Define gender choices available to feed into the :attr:`gender` field.
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
    )
    #: A choice field which accepts only two choices specified in :attr:`GENDER_CHOICES`
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)

    city = models.CharField(max_length=31, null=True, default=None)

    #: Add the custom manager class (:class:`user_auth.manager.UserManager`) which handles user_auth creation.
    objects = UserManager()

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def has_module_perms(self, app_label):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @property
    def is_staff(self):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True

    def has_module_perms(self, app_lable):
        return True