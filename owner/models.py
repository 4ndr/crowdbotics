from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.models import User

class Owner(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'