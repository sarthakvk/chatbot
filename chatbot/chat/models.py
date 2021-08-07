from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.manager import Manager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.username = email
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    first_name = None
    last_name = None

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(_('email address'), blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.email
    def save(self, **kwargs):
        self.username = self.email
        super().save()
    
class ButtonCalls(models.Model):
    dumb_count = models.IntegerField(default=0)
    stupid_count = models.IntegerField(default=0)
    fat_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)