from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    email = models.EmailField(_('email address'), unique=True)
