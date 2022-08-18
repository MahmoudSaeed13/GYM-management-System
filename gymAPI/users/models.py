from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _    
from django_extensions.db.models import TimeStampedModel
from users.utils import set_BMI
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):
    def create_user(self, name, email, username, password=None):
        if not username:
            raise ValueError("user must have username")
        if not name:
            raise ValueError("user must have name")
        if not email:
            raise ValueError("user must have email")
        if not password:
            raise ValueError("user must have password")

        email = self.normalize_email(email=email)
        user = self.model(
            name=name,
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, username, email, name, password=None):
        if not username:
            raise ValueError("user must have username")
        if not name:
            raise ValueError("user must have name")
        if not email:
            raise ValueError("user must have email")
        if not password:
            raise ValueError("user must have password")

        email = self.normalize_email(email=email)
        user = self.model(
            name=name,
            username=username,
            email=email
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

AUTH_PROVIDERS = {'google':"google"}

class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("User full name"),max_length=155)
    username = models.CharField(_("Username"),max_length=155, unique=True)
    email = models.CharField(_("Email"),max_length=155, unique=True)
    is_superuser = models.BooleanField(_("Is user a superuser"), default=False)
    is_verified = models.BooleanField(_("Is user verified email"), default=False)
    is_active = models.BooleanField(_("Is user account activated"),default=True)
    is_staff = models.BooleanField(_("Is user a staff member"),default=False)
    auth_provider = models.CharField(max_length=255, null=True, default=AUTH_PROVIDERS.get("email"))


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name"]

    objects = UserManager()

    def tokens(self):
        token = RefreshToken.for_user(self)
        return {
            "refresh": str(token),
            "access": str(token.access_token) 
        }

    def __str__(self):
        return f"{self.username}"


class ProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("user").order_by("id")
class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    phone = models.CharField(_("Phone Number"),max_length=20, unique=True, null=True)
    age = models.IntegerField(_("Age"), null=True)
    weight = models.DecimalField(_("Weight"),max_digits=5, decimal_places=2, null=True)
    height = models.IntegerField(_("Height"), null=True)
    bmi = models.DecimalField(_('Body Mass Index(BMI)'),max_digits=4, decimal_places=2, null=True)
    image = models.ImageField(upload_to="users/images", default="users/images/default-avatar.png", null=True)
    gender = models.CharField(_("Gender"),max_length=10, choices=(('male', 'Male'),('female', 'Female')), null=True)

    def save(self, *args, **kwargs):
        set_BMI(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Profile: {self.user}"