from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from portal.models import Department


class CustomUser(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    patronymic = models.CharField(max_length=20, verbose_name='Отчество', blank=False)
    email = models.EmailField(_('email address'), unique=True, blank=False)
    photo = models.ImageField(upload_to='photos', blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic} ({self.username})'


class HeadDepartment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Руководитель', blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Департамент', blank=False)

    class Meta:
        verbose_name = 'Руководитель депортамента'
        verbose_name_plural = 'Руководители депортаментов'
